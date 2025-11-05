using System.Collections.Generic;
using System.Linq;
using System.Text.Json;

namespace QtModel.Core;

public record Node(int NodeId, double X, double Y, double Z)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["x"] = X,
        ["y"] = Y,
        ["z"] = Z
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class Element
{
    public Element(int index, string elementType, IReadOnlyList<int> nodeList, int materialId, int sectionId,
        double beta = 0, int initialType = 1, double initialValue = 0)
    {
        Index = index;
        ElementType = elementType;
        NodeList = nodeList;
        MaterialId = materialId;
        SectionId = sectionId;
        Beta = beta;
        InitialType = initialType;
        InitialValue = initialValue;
    }

    public int Index { get; }
    public string ElementType { get; }
    public IReadOnlyList<int> NodeList { get; }
    public int MaterialId { get; }
    public int SectionId { get; }
    public double Beta { get; }
    public int InitialType { get; }
    public double InitialValue { get; }

    public Dictionary<string, object?> ToDictionary()
    {
        var dict = new Dictionary<string, object?>
        {
            ["index"] = Index,
            ["ele_type"] = ElementType,
            ["node_list"] = NodeList,
            ["mat_id"] = MaterialId,
            ["beta"] = Beta
        };

        switch (ElementType.ToUpperInvariant())
        {
            case "CABLE":
                dict["sec_id"] = SectionId;
                dict["initial_type"] = InitialType;
                dict["initial_value"] = InitialValue;
                break;
            case "PLATE":
                dict["thick_id"] = SectionId;
                break;
            default:
                dict["sec_id"] = SectionId;
                break;
        }

        return dict;
    }

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class Material
{
    public Material(int materialId, string name, string materialType, string standard, string database,
        IReadOnlyList<double>? dataInfo = null, bool modified = false, double constructFactor = 1.0,
        int creepId = -1, double fCuk = 0)
    {
        MaterialId = materialId;
        Name = name;
        MaterialType = materialType;
        Standard = standard;
        Database = database;
        DataInfo = dataInfo;
        Modified = modified;
        ConstructFactor = constructFactor;
        CreepId = creepId;
        FCuk = fCuk;
    }

    public int MaterialId { get; }
    public string Name { get; }
    public string MaterialType { get; }
    public string Standard { get; }
    public string Database { get; }
    public IReadOnlyList<double>? DataInfo { get; }
    public bool Modified { get; }
    public double ConstructFactor { get; }
    public int CreepId { get; }
    public double FCuk { get; }

    public Dictionary<string, object?> ToDictionary() => new()
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

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class GeneralSupport
{
    public GeneralSupport(int supportId = 1, int nodeId = 1,
        IReadOnlyList<bool>? boundaryInfo = null, string groupName = "默认边界组", int nodeSystem = 1)
    {
        SupportId = supportId;
        NodeId = nodeId;
        BoundaryInfo = boundaryInfo;
        GroupName = groupName;
        NodeSystem = nodeSystem;
    }

    public int SupportId { get; }
    public int NodeId { get; }
    public IReadOnlyList<bool>? BoundaryInfo { get; }
    public string GroupName { get; }
    public int NodeSystem { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["support_id"] = SupportId,
        ["node_id"] = NodeId,
        ["boundary_info"] = BoundaryInfo,
        ["group_name"] = GroupName,
        ["node_system"] = NodeSystem
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class ElasticLink
{
    public ElasticLink(int linkId, int linkType, int startId, int endId, double betaAngle = 0,
        IReadOnlyList<double>? boundaryInfo = null, string groupName = "默认边界组", double disRatio = 0,
        double kx = 0)
    {
        LinkId = linkId;
        LinkType = linkType;
        StartId = startId;
        EndId = endId;
        BetaAngle = betaAngle;
        BoundaryInfo = boundaryInfo;
        GroupName = groupName;
        DisRatio = disRatio;
        Kx = kx;
    }

    public int LinkId { get; }
    public int LinkType { get; }
    public int StartId { get; }
    public int EndId { get; }
    public double BetaAngle { get; }
    public IReadOnlyList<double>? BoundaryInfo { get; }
    public string GroupName { get; }
    public double DisRatio { get; }
    public double Kx { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["link_id"] = LinkId,
        ["link_type"] = LinkType,
        ["start_id"] = StartId,
        ["end_id"] = EndId,
        ["beta_angle"] = BetaAngle,
        ["boundary_info"] = BoundaryInfo,
        ["group_name"] = GroupName,
        ["dis_ratio"] = DisRatio,
        ["kx"] = Kx
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class ElasticSupport
{
    public ElasticSupport(int supportId, int nodeId, int supportType,
        IReadOnlyList<double>? boundaryInfo = null, string groupName = "默认边界组", int nodeSystem = 1)
    {
        SupportId = supportId;
        NodeId = nodeId;
        SupportType = supportType;
        BoundaryInfo = boundaryInfo;
        GroupName = groupName;
        NodeSystem = nodeSystem;
    }

    public int SupportId { get; }
    public int NodeId { get; }
    public int SupportType { get; }
    public IReadOnlyList<double>? BoundaryInfo { get; }
    public string GroupName { get; }
    public int NodeSystem { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["support_id"] = SupportId,
        ["node_id"] = NodeId,
        ["support_type"] = SupportType,
        ["boundary_info"] = BoundaryInfo,
        ["group_name"] = GroupName,
        ["node_system"] = NodeSystem
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class MasterSlaveLink
{
    public MasterSlaveLink(int linkId, int masterId, int slaveId,
        IReadOnlyList<bool>? boundaryInfo = null, string groupName = "默认边界组")
    {
        LinkId = linkId;
        MasterId = masterId;
        SlaveId = slaveId;
        BoundaryInfo = boundaryInfo;
        GroupName = groupName;
    }

    public int LinkId { get; }
    public int MasterId { get; }
    public int SlaveId { get; }
    public IReadOnlyList<bool>? BoundaryInfo { get; }
    public string GroupName { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["link_id"] = LinkId,
        ["master_id"] = MasterId,
        ["slave_id"] = SlaveId,
        ["boundary_info"] = BoundaryInfo,
        ["group_name"] = GroupName
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class ConstraintEquation
{
    public ConstraintEquation(int constraintId, string name, int secondaryNode, int secondaryDof = 1,
        IReadOnlyList<(int masterNode, int masterDof, double coefficient)>? masterInfo = null,
        string groupName = "默认边界组")
    {
        ConstraintId = constraintId;
        Name = name;
        SecondaryNode = secondaryNode;
        SecondaryDof = secondaryDof;
        MasterInfo = masterInfo;
        GroupName = groupName;
    }

    public int ConstraintId { get; }
    public string Name { get; }
    public int SecondaryNode { get; }
    public int SecondaryDof { get; }
    public IReadOnlyList<(int masterNode, int masterDof, double coefficient)>? MasterInfo { get; }
    public string GroupName { get; }

    public Dictionary<string, object?> ToDictionary()
    {
        object? masterInfoValue = MasterInfo is null
            ? null
            : MasterInfo.Select(info => new Dictionary<string, object>
            {
                ["master_node"] = info.masterNode,
                ["master_dof"] = info.masterDof,
                ["coefficient"] = info.coefficient
            }).ToList();

        return new Dictionary<string, object?>
        {
            ["constraint_id"] = ConstraintId,
            ["name"] = Name,
            ["sec_node"] = SecondaryNode,
            ["sec_dof"] = SecondaryDof,
            ["master_info"] = masterInfoValue,
            ["group_name"] = GroupName
        };
    }

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class BeamConstraint
{
    public BeamConstraint(int constraintId, int beamId, IReadOnlyList<bool>? infoI = null,
        IReadOnlyList<bool>? infoJ = null, string groupName = "默认边界组")
    {
        ConstraintId = constraintId;
        BeamId = beamId;
        InfoI = infoI;
        InfoJ = infoJ;
        GroupName = groupName;
    }

    public int ConstraintId { get; }
    public int BeamId { get; }
    public IReadOnlyList<bool>? InfoI { get; }
    public IReadOnlyList<bool>? InfoJ { get; }
    public string GroupName { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["constraint_id"] = ConstraintId,
        ["beam_id"] = BeamId,
        ["info_i"] = InfoI,
        ["info_j"] = InfoJ,
        ["group_name"] = GroupName
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class NodalLocalAxis
{
    public NodalLocalAxis(int nodeId, (double X, double Y, double Z)? vectorX = null,
        (double X, double Y, double Z)? vectorY = null)
    {
        NodeId = nodeId;
        VectorX = vectorX;
        VectorY = vectorY;
    }

    public int NodeId { get; }
    public (double X, double Y, double Z)? VectorX { get; }
    public (double X, double Y, double Z)? VectorY { get; }

    private static double[]? ToArray((double X, double Y, double Z)? tuple) => tuple is null
        ? null
        : new[] { tuple.Value.X, tuple.Value.Y, tuple.Value.Z };

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["vector_x"] = ToArray(VectorX),
        ["vector_y"] = ToArray(VectorY)
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class PreStressLoad
{
    public PreStressLoad(string caseName, string tendonName, int tensionType, double force,
        string groupName = "默认荷载组")
    {
        CaseName = caseName;
        TendonName = tendonName;
        TensionType = tensionType;
        Force = force;
        GroupName = groupName;
    }

    public string CaseName { get; }
    public string TendonName { get; }
    public int TensionType { get; }
    public double Force { get; }
    public string GroupName { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["case_name"] = CaseName,
        ["tendon_name"] = TendonName,
        ["tension_type"] = TensionType,
        ["force"] = Force,
        ["group_name"] = GroupName
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class NodalMass
{
    public NodalMass(int nodeId, IReadOnlyList<double>? massInfo = null)
    {
        NodeId = nodeId;
        MassInfo = massInfo;
    }

    public int NodeId { get; }
    public IReadOnlyList<double>? MassInfo { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["mass_info"] = MassInfo
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class NodalForce
{
    public NodalForce(int nodeId, string caseName, IReadOnlyList<double>? loadInfo = null,
        string groupName = "默认荷载组")
    {
        NodeId = nodeId;
        CaseName = caseName;
        LoadInfo = loadInfo;
        GroupName = groupName;
    }

    public int NodeId { get; }
    public string CaseName { get; }
    public IReadOnlyList<double>? LoadInfo { get; }
    public string GroupName { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["case_name"] = CaseName,
        ["load_info"] = LoadInfo,
        ["group_name"] = GroupName
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class NodalForceDisplacement
{
    public NodalForceDisplacement(int nodeId, string caseName, int dof, double displacement,
        double load, string groupName = "默认荷载组")
    {
        NodeId = nodeId;
        CaseName = caseName;
        DegreeOfFreedom = dof;
        Displacement = displacement;
        Load = load;
        GroupName = groupName;
    }

    public int NodeId { get; }
    public string CaseName { get; }
    public int DegreeOfFreedom { get; }
    public double Displacement { get; }
    public double Load { get; }
    public string GroupName { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["case_name"] = CaseName,
        ["dof"] = DegreeOfFreedom,
        ["displacement"] = Displacement,
        ["load"] = Load,
        ["group_name"] = GroupName
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class BeamElementLoad
{
    public BeamElementLoad(int elementId, string caseName, int loadType, int coordSystem,
        IReadOnlyList<double>? listX = null, IReadOnlyList<double>? listLoad = null,
        string groupName = "默认荷载组", double loadBias = 0, bool projected = false)
    {
        ElementId = elementId;
        CaseName = caseName;
        LoadType = loadType;
        CoordSystem = coordSystem;
        ListX = listX;
        ListLoad = listLoad;
        GroupName = groupName;
        LoadBias = loadBias;
        Projected = projected;
    }

    public int ElementId { get; }
    public string CaseName { get; }
    public int LoadType { get; }
    public int CoordSystem { get; }
    public IReadOnlyList<double>? ListX { get; }
    public IReadOnlyList<double>? ListLoad { get; }
    public string GroupName { get; }
    public double LoadBias { get; }
    public bool Projected { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["load_type"] = LoadType,
        ["coord_system"] = CoordSystem,
        ["list_x"] = ListX,
        ["list_load"] = ListLoad,
        ["group_name"] = GroupName,
        ["load_bias"] = LoadBias,
        ["projected"] = Projected
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class PlateElementLoad
{
    public PlateElementLoad(int elementId, string caseName, int loadType, int loadPlace, int coordSystem,
        string groupName = "默认荷载组", IReadOnlyList<double>? loadList = null,
        (double X, double Y)? xyList = null)
    {
        ElementId = elementId;
        CaseName = caseName;
        LoadType = loadType;
        LoadPlace = loadPlace;
        CoordSystem = coordSystem;
        GroupName = groupName;
        LoadList = loadList;
        XyList = xyList;
    }

    public int ElementId { get; }
    public string CaseName { get; }
    public int LoadType { get; }
    public int LoadPlace { get; }
    public int CoordSystem { get; }
    public string GroupName { get; }
    public IReadOnlyList<double>? LoadList { get; }
    public (double X, double Y)? XyList { get; }

    private static double[]? ToArray((double X, double Y)? xy) => xy is null
        ? null
        : new[] { xy.Value.X, xy.Value.Y };

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["load_type"] = LoadType,
        ["load_place"] = LoadPlace,
        ["coord_system"] = CoordSystem,
        ["group_name"] = GroupName,
        ["load_list"] = LoadList,
        ["xy_list"] = ToArray(XyList)
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class InitialTension
{
    public InitialTension(int elementId, string caseName, string groupName, double tension, int tensionType)
    {
        ElementId = elementId;
        CaseName = caseName;
        GroupName = groupName;
        Tension = tension;
        TensionType = tensionType;
    }

    public int ElementId { get; }
    public string CaseName { get; }
    public string GroupName { get; }
    public double Tension { get; }
    public int TensionType { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["group_name"] = GroupName,
        ["tension"] = Tension,
        ["tension_type"] = TensionType
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class CableLengthLoad
{
    public CableLengthLoad(int elementId, string caseName, string groupName, double length, int tensionType)
    {
        ElementId = elementId;
        CaseName = caseName;
        GroupName = groupName;
        Length = length;
        TensionType = tensionType;
    }

    public int ElementId { get; }
    public string CaseName { get; }
    public string GroupName { get; }
    public double Length { get; }
    public int TensionType { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["group_name"] = GroupName,
        ["length"] = Length,
        ["tension_type"] = TensionType
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class DeviationParameter
{
    public DeviationParameter(string name, int elementType = 1, IReadOnlyList<double>? parameters = null)
    {
        Name = name;
        ElementType = elementType;
        Parameters = parameters;
    }

    public string Name { get; }
    public int ElementType { get; }
    public IReadOnlyList<double>? Parameters { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["name"] = Name,
        ["element_type"] = ElementType,
        ["parameters"] = Parameters
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class DeviationLoad
{
    public DeviationLoad(string caseName, string deviationName, int loadType, double amplitude,
        string groupName = "默认荷载组")
    {
        CaseName = caseName;
        DeviationName = deviationName;
        LoadType = loadType;
        Amplitude = amplitude;
        GroupName = groupName;
    }

    public string CaseName { get; }
    public string DeviationName { get; }
    public int LoadType { get; }
    public double Amplitude { get; }
    public string GroupName { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["case_name"] = CaseName,
        ["deviation_name"] = DeviationName,
        ["load_type"] = LoadType,
        ["amplitude"] = Amplitude,
        ["group_name"] = GroupName
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class ElementTemperature
{
    public ElementTemperature(int elementId, string caseName, int loadType, IReadOnlyList<double>? temperatures = null,
        string groupName = "默认荷载组")
    {
        ElementId = elementId;
        CaseName = caseName;
        LoadType = loadType;
        Temperatures = temperatures;
        GroupName = groupName;
    }

    public int ElementId { get; }
    public string CaseName { get; }
    public int LoadType { get; }
    public IReadOnlyList<double>? Temperatures { get; }
    public string GroupName { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["case_name"] = CaseName,
        ["load_type"] = LoadType,
        ["temperature"] = Temperatures,
        ["group_name"] = GroupName
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class GradientTemperature
{
    public GradientTemperature(string caseName, string groupName, int gradientType,
        IReadOnlyList<double>? gradientInfo = null)
    {
        CaseName = caseName;
        GroupName = groupName;
        GradientType = gradientType;
        GradientInfo = gradientInfo;
    }

    public string CaseName { get; }
    public string GroupName { get; }
    public int GradientType { get; }
    public IReadOnlyList<double>? GradientInfo { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["case_name"] = CaseName,
        ["group_name"] = GroupName,
        ["gradient_type"] = GradientType,
        ["gradient_info"] = GradientInfo
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class BeamSectionTemperature
{
    public BeamSectionTemperature(string caseName, string groupName, string secName,
        IReadOnlyList<double>? tempList = null)
    {
        CaseName = caseName;
        GroupName = groupName;
        SectionName = secName;
        TemperatureList = tempList;
    }

    public string CaseName { get; }
    public string GroupName { get; }
    public string SectionName { get; }
    public IReadOnlyList<double>? TemperatureList { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["case_name"] = CaseName,
        ["group_name"] = GroupName,
        ["sec_name"] = SectionName,
        ["temp_list"] = TemperatureList
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class IndexTemperature
{
    public IndexTemperature(string caseName, string groupName, int index, double temperature)
    {
        CaseName = caseName;
        GroupName = groupName;
        Index = index;
        Temperature = temperature;
    }

    public string CaseName { get; }
    public string GroupName { get; }
    public int Index { get; }
    public double Temperature { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["case_name"] = CaseName,
        ["group_name"] = GroupName,
        ["index"] = Index,
        ["temperature"] = Temperature
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class TopPlateTemperature
{
    public TopPlateTemperature(string caseName, string groupName, IReadOnlyList<double>? temperatures = null)
    {
        CaseName = caseName;
        GroupName = groupName;
        Temperatures = temperatures;
    }

    public string CaseName { get; }
    public string GroupName { get; }
    public IReadOnlyList<double>? Temperatures { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["case_name"] = CaseName,
        ["group_name"] = GroupName,
        ["temperature"] = Temperatures
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record SectionLoopSegment(string Type, IReadOnlyList<(double X, double Y)> Points)
{
    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["type"] = Type,
        ["points"] = Points.Select(p => new[] { p.X, p.Y }).ToList()
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record SectionLineSegment(IReadOnlyList<double> Parameters)
{
    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["parameters"] = Parameters
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public class EffectiveWidth
{
    public EffectiveWidth(string secName, IReadOnlyList<double>? widthInfo = null)
    {
        SectionName = secName;
        WidthInfo = widthInfo;
    }

    public string SectionName { get; }
    public IReadOnlyList<double>? WidthInfo { get; }

    public Dictionary<string, object?> ToDictionary() => new()
    {
        ["sec_name"] = SectionName,
        ["width_info"] = WidthInfo
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}
