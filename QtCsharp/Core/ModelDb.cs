using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Encodings.Web;
using System.Text.Json;

namespace QtCsharp.Core;

public abstract class QtModelRecord
{
    protected static readonly JsonSerializerOptions JsonOptions = new()
    {
        WriteIndented = false,
        Encoder = JavaScriptEncoder.UnsafeRelaxedJsonEscaping
    };

    public abstract Dictionary<string, object?> ToDictionary();

    public string ToJson() => JsonSerializer.Serialize(ToDictionary(), JsonOptions);

    public override string ToString() => ToJson();
}

public sealed class Node : QtModelRecord
{
    public int NodeId { get; }
    public double X { get; }
    public double Y { get; }
    public double Z { get; }

    public Node(int nodeId, double x, double y, double z)
    {
        NodeId = nodeId;
        X = x;
        Y = y;
        Z = z;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["x"] = X,
        ["y"] = Y,
        ["z"] = Z
    };
}

public sealed class Element : QtModelRecord
{
    public int Index { get; }
    public string ElementType { get; }
    public IReadOnlyList<int> NodeList { get; }
    public int MaterialId { get; }
    public int SectionId { get; }
    public double Beta { get; }
    public int InitialType { get; }
    public double InitialValue { get; }

    public Element(
        int index,
        string elementType,
        IEnumerable<int> nodeList,
        int matId,
        int secId,
        double beta = 0,
        int initialType = 1,
        double initialValue = 0)
    {
        Index = index;
        ElementType = elementType;
        NodeList = nodeList?.ToArray() ?? Array.Empty<int>();
        MaterialId = matId;
        SectionId = secId;
        Beta = beta;
        InitialType = initialType;
        InitialValue = initialValue;
    }

    public override Dictionary<string, object?> ToDictionary()
    {
        var baseDict = new Dictionary<string, object?>
        {
            ["index"] = Index,
            ["ele_type"] = ElementType,
            ["node_list"] = NodeList,
            ["mat_id"] = MaterialId,
            ["beta"] = Beta
        };

        if (string.Equals(ElementType, "PLATE", StringComparison.OrdinalIgnoreCase))
        {
            baseDict["thick_id"] = SectionId;
        }
        else
        {
            baseDict["sec_id"] = SectionId;
        }

        if (string.Equals(ElementType, "CABLE", StringComparison.OrdinalIgnoreCase))
        {
            baseDict["initial_type"] = InitialType;
            baseDict["initial_value"] = InitialValue;
        }

        return baseDict;
    }
}

public sealed class Material : QtModelRecord
{
    public int MaterialId { get; }
    public string Name { get; }
    public string MaterialType { get; }
    public string Standard { get; }
    public string Database { get; }
    public bool Modified { get; }
    public double ConstructFactor { get; }
    public int CreepId { get; }
    public double FCuk { get; }
    public IReadOnlyList<double>? DataInfo { get; }

    public Material(
        int matId,
        string name,
        string matType,
        string standard,
        string database,
        IEnumerable<double>? dataInfo = null,
        bool modified = false,
        double constructFactor = 1.0,
        int creepId = -1,
        double fCuk = 0)
    {
        MaterialId = matId;
        Name = name;
        MaterialType = matType;
        Standard = standard;
        Database = database;
        DataInfo = dataInfo?.ToArray();
        Modified = modified;
        ConstructFactor = constructFactor;
        CreepId = creepId;
        FCuk = fCuk;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["mat_id"] = MaterialId,
        ["name"] = Name,
        ["mat_type"] = MaterialType,
        ["standard"] = Standard,
        ["database"] = Database,
        ["construct_factor"] = ConstructFactor,
        ["modified"] = Modified,
        ["data_info"] = DataInfo,
        ["is_creep"] = CreepId,
        ["f_cuk"] = FCuk
    };
}

public sealed class GeneralSupport : QtModelRecord
{
    public int SupportId { get; }
    public int NodeId { get; }
    public IReadOnlyList<bool>? BoundaryInfo { get; }
    public string GroupName { get; }
    public int NodeSystem { get; }

    public GeneralSupport(
        int supportId = 1,
        int nodeId = 1,
        IEnumerable<bool>? boundaryInfo = null,
        string groupName = "默认边界组",
        int nodeSystem = 1)
    {
        SupportId = supportId;
        NodeId = nodeId;
        BoundaryInfo = boundaryInfo?.ToArray();
        GroupName = groupName;
        NodeSystem = nodeSystem;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["support_id"] = SupportId,
        ["node_id"] = NodeId,
        ["boundary_info"] = BoundaryInfo,
        ["group_name"] = GroupName,
        ["node_system"] = NodeSystem
    };
}

public sealed class ElasticLink : QtModelRecord
{
    public int LinkId { get; }
    public int LinkType { get; }
    public int StartId { get; }
    public int EndId { get; }
    public double BetaAngle { get; }
    public IReadOnlyList<double>? BoundaryInfo { get; }
    public string GroupName { get; }
    public double DistanceRatio { get; }
    public double Kx { get; }

    public ElasticLink(
        int linkId,
        int linkType,
        int startId,
        int endId,
        double betaAngle = 0,
        IEnumerable<double>? boundaryInfo = null,
        string groupName = "默认边界组",
        double disRatio = 0,
        double kx = 0)
    {
        LinkId = linkId;
        LinkType = linkType;
        StartId = startId;
        EndId = endId;
        BetaAngle = betaAngle;
        BoundaryInfo = boundaryInfo?.ToArray();
        GroupName = groupName;
        DistanceRatio = disRatio;
        Kx = kx;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["link_id"] = LinkId,
        ["link_type"] = LinkType,
        ["start_id"] = StartId,
        ["end_id"] = EndId,
        ["beta_angle"] = BetaAngle,
        ["boundary_info"] = BoundaryInfo,
        ["group_name"] = GroupName,
        ["dis_ratio"] = DistanceRatio,
        ["kx"] = Kx
    };
}

public sealed class ElasticSupport : QtModelRecord
{
    public int SupportId { get; }
    public int NodeId { get; }
    public int SupportType { get; }
    public IReadOnlyList<double>? BoundaryInfo { get; }
    public string GroupName { get; }
    public int NodeSystem { get; }

    public ElasticSupport(
        int supportId,
        int nodeId,
        int supportType,
        IEnumerable<double>? boundaryInfo = null,
        string groupName = "默认边界组",
        int nodeSystem = 1)
    {
        SupportId = supportId;
        NodeId = nodeId;
        SupportType = supportType;
        BoundaryInfo = boundaryInfo?.ToArray();
        GroupName = groupName;
        NodeSystem = nodeSystem;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["support_id"] = SupportId,
        ["node_id"] = NodeId,
        ["support_type"] = SupportType,
        ["boundary_info"] = BoundaryInfo,
        ["group_name"] = GroupName,
        ["node_system"] = NodeSystem
    };
}

public sealed class MasterSlaveLink : QtModelRecord
{
    public int LinkId { get; }
    public int MasterId { get; }
    public int SlaveId { get; }
    public IReadOnlyList<bool>? BoundaryInfo { get; }
    public string GroupName { get; }

    public MasterSlaveLink(
        int linkId,
        int masterId,
        int slaveId,
        IEnumerable<bool>? boundaryInfo = null,
        string groupName = "默认边界组")
    {
        LinkId = linkId;
        MasterId = masterId;
        SlaveId = slaveId;
        BoundaryInfo = boundaryInfo?.ToArray();
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["link_id"] = LinkId,
        ["master_id"] = MasterId,
        ["slave_id"] = SlaveId,
        ["boundary_info"] = BoundaryInfo,
        ["group_name"] = GroupName
    };
}

public sealed class ConstraintEquation : QtModelRecord
{
    public int ConstraintId { get; }
    public string Name { get; }
    public int SecondaryNode { get; }
    public int SecondaryDof { get; }
    public IReadOnlyList<(int MasterNode, int MasterDof, double Factor)>? MasterInfo { get; }
    public string GroupName { get; }

    public ConstraintEquation(
        int constraintId,
        string name,
        int secNode,
        int secDof = 1,
        IEnumerable<(int masterNode, int masterDof, double factor)>? masterInfo = null,
        string groupName = "默认边界组")
    {
        ConstraintId = constraintId;
        Name = name;
        SecondaryNode = secNode;
        SecondaryDof = secDof;
        MasterInfo = masterInfo?.ToArray();
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary()
    {
        var masters = MasterInfo?.Select(item => new object[] { item.MasterNode, item.MasterDof, item.Factor }).ToList();
        return new Dictionary<string, object?>
        {
            ["constraint_id"] = ConstraintId,
            ["name"] = Name,
            ["sec_node"] = SecondaryNode,
            ["sec_dof"] = SecondaryDof,
            ["master_info"] = masters,
            ["group_name"] = GroupName
        };
    }
}

public sealed class BeamConstraint : QtModelRecord
{
    public int ConstraintId { get; }
    public int BeamId { get; }
    public IReadOnlyList<bool>? InfoI { get; }
    public IReadOnlyList<bool>? InfoJ { get; }
    public string GroupName { get; }

    public BeamConstraint(
        int constraintId,
        int beamId,
        IEnumerable<bool>? infoI = null,
        IEnumerable<bool>? infoJ = null,
        string groupName = "默认边界组")
    {
        ConstraintId = constraintId;
        BeamId = beamId;
        InfoI = infoI?.ToArray();
        InfoJ = infoJ?.ToArray();
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["constraint_id"] = ConstraintId,
        ["beam_id"] = BeamId,
        ["info_i"] = InfoI,
        ["info_j"] = InfoJ,
        ["group_name"] = GroupName
    };
}

public sealed class NodalLocalAxis : QtModelRecord
{
    public int NodeId { get; }
    public IReadOnlyList<double>? VectorX { get; }
    public IReadOnlyList<double>? VectorY { get; }

    public NodalLocalAxis(
        int nodeId,
        IEnumerable<double>? vectorX = null,
        IEnumerable<double>? vectorY = null)
    {
        NodeId = nodeId;
        VectorX = vectorX?.ToArray();
        VectorY = vectorY?.ToArray();
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["vector_x"] = VectorX,
        ["vector_y"] = VectorY
    };
}

public sealed class PreStressLoad : QtModelRecord
{
    public string CaseName { get; }
    public string TendonName { get; }
    public int TensionType { get; }
    public double Force { get; }
    public string GroupName { get; }

    public PreStressLoad(
        string caseName,
        string tendonName,
        int tensionType,
        double force,
        string groupName = "默认荷载组")
    {
        CaseName = caseName;
        TendonName = tendonName;
        TensionType = tensionType;
        Force = force;
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["case_name"] = CaseName,
        ["tendon_name"] = TendonName,
        ["tension_type"] = TensionType,
        ["force"] = Force,
        ["group_name"] = GroupName
    };
}

public sealed class NodalMass : QtModelRecord
{
    public int NodeId { get; }
    public IReadOnlyList<double>? MassInfo { get; }

    public NodalMass(int nodeId, IEnumerable<double>? massInfo = null)
    {
        NodeId = nodeId;
        MassInfo = massInfo?.ToArray();
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["mass_info"] = MassInfo
    };
}

public sealed class NodalForce : QtModelRecord
{
    public int NodeId { get; }
    public string CaseName { get; }
    public IReadOnlyList<double>? LoadInfo { get; }
    public string GroupName { get; }

    public NodalForce(
        int nodeId,
        string caseName,
        IEnumerable<double>? loadInfo = null,
        string groupName = "默认荷载组")
    {
        NodeId = nodeId;
        CaseName = caseName;
        LoadInfo = loadInfo?.ToArray();
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["case_name"] = CaseName,
        ["load_info"] = LoadInfo,
        ["group_name"] = GroupName
    };
}

public sealed class NodalForceDisplacement : QtModelRecord
{
    public int NodeId { get; }
    public string CaseName { get; }
    public IReadOnlyList<double>? LoadInfo { get; }
    public string GroupName { get; }

    public NodalForceDisplacement(
        int nodeId = 1,
        string caseName = "",
        IEnumerable<double>? loadInfo = null,
        string groupName = "默认荷载组")
    {
        NodeId = nodeId;
        CaseName = caseName;
        LoadInfo = loadInfo?.ToArray();
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["case_name"] = CaseName,
        ["load_info"] = LoadInfo,
        ["group_name"] = GroupName
    };
}

public sealed class BeamLoadBias
{
    public bool IsEccentric { get; }
    public int ReferenceType { get; }
    public int CoordinateSystem { get; }
    public double Distance { get; }

    public BeamLoadBias(bool isEccentric, int referenceType, int coordinateSystem, double distance)
    {
        IsEccentric = isEccentric;
        ReferenceType = referenceType;
        CoordinateSystem = coordinateSystem;
        Distance = distance;
    }
}

public sealed class BeamElementLoad : QtModelRecord
{
    public int BeamId { get; }
    public string CaseName { get; }
    public int LoadType { get; }
    public int CoordinateSystem { get; }
    public IReadOnlyList<double>? PositionList { get; }
    public IReadOnlyList<double>? LoadValues { get; }
    public string GroupName { get; }
    public BeamLoadBias? LoadBias { get; }
    public bool Projected { get; }

    public BeamElementLoad(
        int beamId,
        string caseName,
        int loadType,
        int coordSystem,
        IEnumerable<double>? listX = null,
        IEnumerable<double>? listLoad = null,
        string groupName = "默认荷载组",
        BeamLoadBias? loadBias = null,
        bool projected = false)
    {
        BeamId = beamId;
        CaseName = caseName;
        LoadType = loadType;
        CoordinateSystem = coordSystem;
        PositionList = listX?.ToArray();
        LoadValues = listLoad?.ToArray();
        GroupName = groupName;
        LoadBias = loadBias;
        Projected = projected;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["beam_id"] = BeamId,
        ["case_name"] = CaseName,
        ["load_type"] = LoadType,
        ["coord_system"] = CoordinateSystem,
        ["list_x"] = PositionList,
        ["list_load"] = LoadValues,
        ["group_name"] = GroupName,
        ["load_bias"] = LoadBias,
        ["projected"] = Projected
    };
}

public sealed class PlateElementLoad : QtModelRecord
{
    public int ElementId { get; }
    public string CaseName { get; }
    public int LoadType { get; }
    public int LoadPlace { get; }
    public int CoordinateSystem { get; }
    public string GroupName { get; }
    public IReadOnlyList<double>? LoadList { get; }
    public IReadOnlyList<double>? PositionXY { get; }

    public PlateElementLoad(
        int elementId,
        string caseName,
        int loadType,
        int loadPlace,
        int coordSystem,
        string groupName = "默认荷载组",
        IEnumerable<double>? loadList = null,
        IEnumerable<double>? xyList = null)
    {
        ElementId = elementId;
        CaseName = caseName;
        LoadType = loadType;
        LoadPlace = loadPlace;
        CoordinateSystem = coordSystem;
        GroupName = groupName;
        LoadList = loadList?.ToArray();
        PositionXY = xyList?.ToArray();
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["load_type"] = LoadType,
        ["load_place"] = LoadPlace,
        ["coord_system"] = CoordinateSystem,
        ["group_name"] = GroupName,
        ["load_list"] = LoadList,
        ["xy_list"] = PositionXY
    };
}

public sealed class InitialTension : QtModelRecord
{
    public int ElementId { get; }
    public string CaseName { get; }
    public string GroupName { get; }
    public double Tension { get; }
    public int TensionType { get; }

    public InitialTension(int elementId, string caseName, string groupName, double tension, int tensionType)
    {
        ElementId = elementId;
        CaseName = caseName;
        GroupName = groupName;
        Tension = tension;
        TensionType = tensionType;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["group_name"] = GroupName,
        ["tension"] = Tension,
        ["tension_type"] = TensionType
    };
}

public sealed class CableLengthLoad : QtModelRecord
{
    public int ElementId { get; }
    public string CaseName { get; }
    public string GroupName { get; }
    public double Length { get; }
    public int TensionType { get; }

    public CableLengthLoad(int elementId, string caseName, string groupName, double length, int tensionType)
    {
        ElementId = elementId;
        CaseName = caseName;
        GroupName = groupName;
        Length = length;
        TensionType = tensionType;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["group_name"] = GroupName,
        ["length"] = Length,
        ["tension_type"] = TensionType
    };
}

public sealed class DeviationParameter : QtModelRecord
{
    public string Name { get; }
    public int ElementType { get; }
    public IReadOnlyList<double>? Parameters { get; }

    public DeviationParameter(string name, int elementType = 1, IEnumerable<double>? parameters = null)
    {
        Name = name;
        ElementType = elementType;
        Parameters = parameters?.ToArray();
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["name"] = Name,
        ["element_type"] = ElementType,
        ["parameters"] = Parameters
    };
}

public sealed class DeviationLoad : QtModelRecord
{
    public int ElementId { get; }
    public string CaseName { get; }
    public IReadOnlyList<string>? Parameters { get; }
    public string GroupName { get; }

    public DeviationLoad(
        int elementId,
        string caseName,
        IEnumerable<string>? parameters = null,
        string groupName = "默认荷载组")
    {
        ElementId = elementId;
        CaseName = caseName;
        Parameters = parameters?.ToArray();
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["parameters"] = Parameters,
        ["group_name"] = GroupName
    };
}

public sealed class ElementTemperature : QtModelRecord
{
    public int ElementId { get; }
    public string CaseName { get; }
    public double Temperature { get; }
    public string GroupName { get; }

    public ElementTemperature(int elementId = 1, string caseName = "", double temperature = 1, string groupName = "默认荷载组")
    {
        ElementId = elementId;
        CaseName = caseName;
        Temperature = temperature;
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["temperature"] = Temperature,
        ["group_name"] = GroupName
    };
}

public sealed class GradientTemperature : QtModelRecord
{
    public int ElementId { get; }
    public string CaseName { get; }
    public double Temperature { get; }
    public int SectionOriental { get; }
    public int ElementType { get; }
    public string GroupName { get; }

    public GradientTemperature(
        int elementId,
        string caseName,
        double temperature,
        int sectionOriental = 1,
        int elementType = 1,
        string groupName = "默认荷载组")
    {
        ElementId = elementId;
        CaseName = caseName;
        Temperature = temperature;
        SectionOriental = sectionOriental;
        ElementType = elementType;
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["temperature"] = Temperature,
        ["section_oriental"] = SectionOriental,
        ["element_type"] = ElementType,
        ["group_name"] = GroupName
    };
}

public sealed class BeamSectionTemperature : QtModelRecord
{
    public int ElementId { get; }
    public string CaseName { get; }
    public double PavingThickness { get; }
    public int TemperatureType { get; }
    public int PavingType { get; }
    public string GroupName { get; }
    public bool Modify { get; }
    public IReadOnlyList<double>? TemperatureList { get; }

    public BeamSectionTemperature(
        int elementId,
        string caseName,
        double pavingThick,
        int temperatureType = 1,
        int pavingType = 1,
        string groupName = "默认荷载组",
        bool modify = false,
        IEnumerable<double>? tempList = null)
    {
        ElementId = elementId;
        CaseName = caseName;
        PavingThickness = pavingThick;
        TemperatureType = temperatureType;
        PavingType = pavingType;
        GroupName = groupName;
        Modify = modify;
        TemperatureList = tempList?.ToArray();
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["paving_thick"] = PavingThickness,
        ["temperature_type"] = TemperatureType,
        ["paving_type"] = PavingType,
        ["group_name"] = GroupName,
        ["modify"] = Modify,
        ["temp_list"] = TemperatureList
    };
}

public sealed class IndexTemperature : QtModelRecord
{
    public int ElementId { get; }
    public string CaseName { get; }
    public double Temperature { get; }
    public double Index { get; }
    public string GroupName { get; }

    public IndexTemperature(int elementId, string caseName, double temperature = 0, double index = 1, string groupName = "默认荷载组")
    {
        ElementId = elementId;
        CaseName = caseName;
        Temperature = temperature;
        Index = index;
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["temperature"] = Temperature,
        ["index"] = Index,
        ["group_name"] = GroupName
    };
}

public sealed class TopPlateTemperature : QtModelRecord
{
    public int ElementId { get; }
    public string CaseName { get; }
    public double Temperature { get; }
    public string GroupName { get; }

    public TopPlateTemperature(int elementId, string caseName, double temperature = 0, string groupName = "默认荷载组")
    {
        ElementId = elementId;
        CaseName = caseName;
        Temperature = temperature;
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["temperature"] = Temperature,
        ["group_name"] = GroupName
    };
}

public sealed class SectionLoopSegment : QtModelRecord
{
    public IReadOnlyList<(double X, double Y)> MainLoop { get; }
    public IReadOnlyList<IReadOnlyList<(double X, double Y)>>? SubLoops { get; }

    public SectionLoopSegment(
        IEnumerable<(double X, double Y)> mainLoop,
        IEnumerable<IEnumerable<(double X, double Y)>>? subLoops = null)
    {
        MainLoop = mainLoop?.ToArray() ?? Array.Empty<(double, double)>();
        SubLoops = subLoops?.Select(loop => (IReadOnlyList<(double, double)>)loop.ToArray()).ToArray();
    }

    public override Dictionary<string, object?> ToDictionary()
    {
        var sub = SubLoops?.Select(loop => loop.Select(p => new[] { p.X, p.Y }).ToList()).ToList();
        return new Dictionary<string, object?>
        {
            ["main_loop"] = MainLoop.Select(p => new[] { p.X, p.Y }).ToList(),
            ["sub_loops"] = sub
        };
    }
}

public sealed class SectionLineSegment : QtModelRecord
{
    public (double X, double Y) PointStart { get; }
    public (double X, double Y) PointEnd { get; }
    public double Thickness { get; }

    public SectionLineSegment((double X, double Y) pointStart, (double X, double Y) pointEnd, double thickness)
    {
        PointStart = pointStart;
        PointEnd = pointEnd;
        Thickness = thickness;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["point_start"] = new[] { PointStart.X, PointStart.Y },
        ["point_end"] = new[] { PointEnd.X, PointEnd.Y },
        ["thickness"] = Thickness
    };
}

public sealed class EffectiveWidth : QtModelRecord
{
    public int Index { get; }
    public int ElementId { get; }
    public double IyI { get; }
    public double IyJ { get; }
    public double FactorI { get; }
    public double FactorJ { get; }
    public double DzI { get; }
    public double DzJ { get; }
    public string GroupName { get; }

    public EffectiveWidth(
        int index,
        int elementId,
        double iyI,
        double iyJ,
        double factorI,
        double factorJ,
        double dzI,
        double dzJ,
        string groupName)
    {
        Index = index;
        ElementId = elementId;
        IyI = iyI;
        IyJ = iyJ;
        FactorI = factorI;
        FactorJ = factorJ;
        DzI = dzI;
        DzJ = dzJ;
        GroupName = groupName;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["index"] = Index,
        ["element_id"] = ElementId,
        ["iy_i"] = IyI,
        ["iy_j"] = IyJ,
        ["factor_i"] = FactorI,
        ["factor_j"] = FactorJ,
        ["dz_i"] = DzI,
        ["dz_j"] = DzJ,
        ["group_name"] = GroupName
    };
}
