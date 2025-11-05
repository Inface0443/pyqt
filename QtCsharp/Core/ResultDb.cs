using System;
using System.Collections.Generic;
using System.Linq;

namespace QtCsharp.Core;

public sealed class NodeDisplacement : QtModelRecord
{
    public int NodeId { get; }
    public double Time { get; }
    public double Dx { get; }
    public double Dy { get; }
    public double Dz { get; }
    public double Rx { get; }
    public double Ry { get; }
    public double Rz { get; }

    public NodeDisplacement(int nodeId, IEnumerable<double> displacements, double time = 0)
    {
        var list = displacements?.ToArray() ?? throw new ArgumentNullException(nameof(displacements));
        if (list.Length != 6)
        {
            throw new ArgumentException("操作错误: 'displacements' 列表有误", nameof(displacements));
        }

        NodeId = nodeId;
        Time = time;
        Dx = list[0];
        Dy = list[1];
        Dz = list[2];
        Rx = list[3];
        Ry = list[4];
        Rz = list[5];
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["time"] = Time,
        ["dx"] = Dx,
        ["dy"] = Dy,
        ["dz"] = Dz,
        ["rx"] = Rx,
        ["ry"] = Ry,
        ["rz"] = Rz
    };
}

public sealed class SupportReaction : QtModelRecord
{
    public int NodeId { get; }
    public double Time { get; }
    public double Fx { get; }
    public double Fy { get; }
    public double Fz { get; }
    public double Mx { get; }
    public double My { get; }
    public double Mz { get; }

    public SupportReaction(int nodeId, IEnumerable<double> force, double time = 0)
    {
        var list = force?.ToArray() ?? throw new ArgumentNullException(nameof(force));
        if (list.Length != 6)
        {
            throw new ArgumentException("操作错误: 'force' 列表有误", nameof(force));
        }

        NodeId = nodeId;
        Time = time;
        Fx = list[0];
        Fy = list[1];
        Fz = list[2];
        Mx = list[3];
        My = list[4];
        Mz = list[5];
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["node_id"] = NodeId,
        ["time"] = Time,
        ["fx"] = Fx,
        ["fy"] = Fy,
        ["fz"] = Fz,
        ["mx"] = Mx,
        ["my"] = My,
        ["mz"] = Mz
    };
}

public sealed class BeamElementForce : QtModelRecord
{
    public int ElementId { get; }
    public double Time { get; }
    public Force ForceI { get; }
    public Force ForceJ { get; }

    public BeamElementForce(int elementId, IEnumerable<double> forceI, IEnumerable<double> forceJ, double time = 0)
    {
        var listI = forceI?.ToArray() ?? throw new ArgumentNullException(nameof(forceI));
        var listJ = forceJ?.ToArray() ?? throw new ArgumentNullException(nameof(forceJ));
        if (listI.Length != 6 || listJ.Length != 6)
        {
            throw new ArgumentException("操作错误: 'force_i' and 'force_j' 列表有误");
        }

        ElementId = elementId;
        Time = time;
        ForceI = new Force(listI[0], listI[1], listI[2], listI[3], listI[4], listI[5]);
        ForceJ = new Force(listJ[0], listJ[1], listJ[2], listJ[3], listJ[4], listJ[5]);
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["time"] = Time,
        ["force_i"] = ForceI.ToDictionary(),
        ["force_j"] = ForceJ.ToDictionary()
    };
}

public sealed class TrussElementForce : QtModelRecord
{
    public int ElementId { get; }
    public double Time { get; }
    public double Ni { get; }
    public double Fxi { get; }
    public double Fyi { get; }
    public double Fzi { get; }
    public double Nj { get; }
    public double Fxj { get; }
    public double Fyj { get; }
    public double Fzj { get; }

    public TrussElementForce(int elementId, IEnumerable<double> forceI, IEnumerable<double> forceJ, double time = 0)
    {
        var listI = forceI?.ToArray() ?? throw new ArgumentNullException(nameof(forceI));
        var listJ = forceJ?.ToArray() ?? throw new ArgumentNullException(nameof(forceJ));
        if (listI.Length != 6 || listJ.Length != 6)
        {
            throw new ArgumentException("操作错误: 'force_i' and 'force_j' 列表有误");
        }

        ElementId = elementId;
        Time = time;
        Ni = listI[3];
        Fxi = listI[0];
        Fyi = listI[1];
        Fzi = listI[2];
        Nj = listJ[3];
        Fxj = listJ[0];
        Fyj = listJ[1];
        Fzj = listJ[2];
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["time"] = Time,
        ["Ni"] = Ni,
        ["Fxi"] = Fxi,
        ["Fyi"] = Fyi,
        ["Fzi"] = Fzi,
        ["Nj"] = Nj,
        ["Fxj"] = Fxj,
        ["Fyj"] = Fyj,
        ["Fzj"] = Fzj
    };
}

public sealed class ShellElementForce : QtModelRecord
{
    public int ElementId { get; }
    public double Time { get; }
    public Force ForceI { get; }
    public Force ForceJ { get; }
    public Force ForceK { get; }
    public Force ForceL { get; }

    public ShellElementForce(
        int elementId,
        IEnumerable<double> forceI,
        IEnumerable<double> forceJ,
        IEnumerable<double> forceK,
        IEnumerable<double> forceL,
        double time = 0)
    {
        var listI = forceI?.ToArray() ?? throw new ArgumentNullException(nameof(forceI));
        var listJ = forceJ?.ToArray() ?? throw new ArgumentNullException(nameof(forceJ));
        var listK = forceK?.ToArray() ?? throw new ArgumentNullException(nameof(forceK));
        var listL = forceL?.ToArray() ?? throw new ArgumentNullException(nameof(forceL));
        if (listI.Length != 6 || listJ.Length != 6 || listK.Length != 6 || listL.Length != 6)
        {
            throw new ArgumentException("操作错误:  内力列表有误");
        }

        ElementId = elementId;
        Time = time;
        ForceI = new Force(listI[0], listI[1], listI[2], listI[3], listI[4], listI[5]);
        ForceJ = new Force(listJ[0], listJ[1], listJ[2], listJ[3], listJ[4], listJ[5]);
        ForceK = new Force(listK[0], listK[1], listK[2], listK[3], listK[4], listK[5]);
        ForceL = new Force(listL[0], listL[1], listL[2], listL[3], listL[4], listL[5]);
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["time"] = Time,
        ["force_i"] = ForceI.ToDictionary(),
        ["force_j"] = ForceJ.ToDictionary(),
        ["force_k"] = ForceK.ToDictionary(),
        ["force_l"] = ForceL.ToDictionary()
    };
}

public sealed class CompositeElementForce : QtModelRecord
{
    public int ElementId { get; }
    public Force ForceI { get; }
    public Force ForceJ { get; }
    public double ShearForce { get; }
    public Force MainForceI { get; }
    public Force MainForceJ { get; }
    public Force SubForceI { get; }
    public Force SubForceJ { get; }
    public bool IsComposite { get; }

    public CompositeElementForce(
        int elementId,
        IEnumerable<double> forceI,
        IEnumerable<double> forceJ,
        double shearForce,
        IEnumerable<double> mainForceI,
        IEnumerable<double> mainForceJ,
        IEnumerable<double> subForceI,
        IEnumerable<double> subForceJ,
        bool isComposite)
    {
        var listI = forceI?.ToArray() ?? throw new ArgumentNullException(nameof(forceI));
        var listJ = forceJ?.ToArray() ?? throw new ArgumentNullException(nameof(forceJ));
        if (listI.Length != 6 || listJ.Length != 6)
        {
            throw new ArgumentException("操作错误: 'force_i' and 'force_j' 列表有误");
        }

        ElementId = elementId;
        ForceI = new Force(listI[0], listI[1], listI[2], listI[3], listI[4], listI[5]);
        ForceJ = new Force(listJ[0], listJ[1], listJ[2], listJ[3], listJ[4], listJ[5]);
        ShearForce = shearForce;
        MainForceI = ForceFromEnumerable(mainForceI);
        MainForceJ = ForceFromEnumerable(mainForceJ);
        SubForceI = ForceFromEnumerable(subForceI);
        SubForceJ = ForceFromEnumerable(subForceJ);
        IsComposite = isComposite;
    }

    private static Force ForceFromEnumerable(IEnumerable<double> values)
    {
        var list = values?.ToArray() ?? throw new ArgumentNullException(nameof(values));
        if (list.Length != 6)
        {
            throw new ArgumentException("操作错误: 内力列表有误");
        }
        return new Force(list[0], list[1], list[2], list[3], list[4], list[5]);
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["force_i"] = ForceI.ToDictionary(),
        ["force_j"] = ForceJ.ToDictionary(),
        ["shear_force"] = ShearForce,
        ["main_force_i"] = MainForceI.ToDictionary(),
        ["main_force_j"] = MainForceJ.ToDictionary(),
        ["sub_force_i"] = SubForceI.ToDictionary(),
        ["sub_force_j"] = SubForceJ.ToDictionary(),
        ["is_composite"] = IsComposite
    };
}

public sealed class BeamElementStress : QtModelRecord
{
    public int ElementId { get; }
    public BeamStress StressI { get; }
    public BeamStress StressJ { get; }

    public BeamElementStress(int elementId, IEnumerable<double> stressI, IEnumerable<double> stressJ)
    {
        var listI = stressI?.ToArray() ?? throw new ArgumentNullException(nameof(stressI));
        var listJ = stressJ?.ToArray() ?? throw new ArgumentNullException(nameof(stressJ));
        if (listI.Length != 9 || listJ.Length != 9)
        {
            throw new ArgumentException("操作错误:  单元应力列表有误");
        }

        ElementId = elementId;
        StressI = new BeamStress(listI);
        StressJ = new BeamStress(listJ);
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["stress_i"] = StressI.ToDictionary(),
        ["stress_j"] = StressJ.ToDictionary()
    };
}

public sealed class ShellElementStress : QtModelRecord
{
    public int ElementId { get; }
    public ShellStress StressITop { get; }
    public ShellStress StressJTop { get; }
    public ShellStress StressKTop { get; }
    public ShellStress StressLTop { get; }
    public ShellStress StressIBot { get; }
    public ShellStress StressJBot { get; }
    public ShellStress StressKBot { get; }
    public ShellStress StressLBot { get; }

    public ShellElementStress(
        int elementId,
        IEnumerable<double> stressITop,
        IEnumerable<double> stressJTop,
        IEnumerable<double> stressKTop,
        IEnumerable<double> stressLTop,
        IEnumerable<double> stressIBot,
        IEnumerable<double> stressJBot,
        IEnumerable<double> stressKBot,
        IEnumerable<double> stressLBot)
    {
        ElementId = elementId;
        StressITop = CreateShellStress(stressITop);
        StressJTop = CreateShellStress(stressJTop);
        StressKTop = CreateShellStress(stressKTop);
        StressLTop = CreateShellStress(stressLTop);
        StressIBot = CreateShellStress(stressIBot);
        StressJBot = CreateShellStress(stressJBot);
        StressKBot = CreateShellStress(stressKBot);
        StressLBot = CreateShellStress(stressLBot);
    }

    private static ShellStress CreateShellStress(IEnumerable<double> values)
    {
        var list = values?.ToArray() ?? throw new ArgumentNullException(nameof(values));
        if (list.Length != 5)
        {
            throw new ArgumentException("操作错误:  单元应力列表有误");
        }
        return new ShellStress(list[0], list[1], list[2], list[3], list[4]);
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["stress_i_top"] = StressITop.ToDictionary(),
        ["stress_j_top"] = StressJTop.ToDictionary(),
        ["stress_k_top"] = StressKTop.ToDictionary(),
        ["stress_l_top"] = StressLTop.ToDictionary(),
        ["stress_i_bot"] = StressIBot.ToDictionary(),
        ["stress_j_bot"] = StressJBot.ToDictionary(),
        ["stress_k_bot"] = StressKBot.ToDictionary(),
        ["stress_l_bot"] = StressLBot.ToDictionary()
    };
}

public sealed class TrussElementStress : QtModelRecord
{
    public int ElementId { get; }
    public double Si { get; }
    public double Sj { get; }

    public TrussElementStress(int elementId, double si, double sj)
    {
        ElementId = elementId;
        Si = si;
        Sj = sj;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["Si"] = Si,
        ["Sj"] = Sj
    };
}

public sealed class CompositeBeamStress : QtModelRecord
{
    public int ElementId { get; }
    public BeamStress MainStressI { get; }
    public BeamStress MainStressJ { get; }
    public BeamStress SubStressI { get; }
    public BeamStress SubStressJ { get; }

    public CompositeBeamStress(
        int elementId,
        IEnumerable<double> mainStressI,
        IEnumerable<double> mainStressJ,
        IEnumerable<double> subStressI,
        IEnumerable<double> subStressJ)
    {
        ElementId = elementId;
        MainStressI = new BeamStress(mainStressI?.ToArray() ?? throw new ArgumentNullException(nameof(mainStressI)));
        MainStressJ = new BeamStress(mainStressJ?.ToArray() ?? throw new ArgumentNullException(nameof(mainStressJ)));
        SubStressI = new BeamStress(subStressI?.ToArray() ?? throw new ArgumentNullException(nameof(subStressI)));
        SubStressJ = new BeamStress(subStressJ?.ToArray() ?? throw new ArgumentNullException(nameof(subStressJ)));
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["main_stress_i"] = MainStressI.ToDictionary(),
        ["main_stress_j"] = MainStressJ.ToDictionary(),
        ["sub_stress_i"] = SubStressI.ToDictionary(),
        ["sub_stress_j"] = SubStressJ.ToDictionary()
    };
}

public sealed class Force : QtModelRecord
{
    public double Fx { get; }
    public double Fy { get; }
    public double Fz { get; }
    public double Mx { get; }
    public double My { get; }
    public double Mz { get; }
    public double Fxyz { get; }
    public double Mxyz { get; }

    public Force(double fx, double fy, double fz, double mx, double my, double mz)
    {
        Fx = fx;
        Fy = fy;
        Fz = fz;
        Mx = mx;
        My = my;
        Mz = mz;
        Fxyz = Math.Sqrt(fx * fx + fy * fy + fz * fz);
        Mxyz = Math.Sqrt(mx * mx + my * my + mz * mz);
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["fx"] = Fx,
        ["fy"] = Fy,
        ["fz"] = Fz,
        ["mx"] = Mx,
        ["my"] = My,
        ["mz"] = Mz,
        ["f_xyz"] = Fxyz,
        ["m_xyz"] = Mxyz
    };
}

public sealed class ShellStress : QtModelRecord
{
    public double Sx { get; }
    public double Sy { get; }
    public double Sxy { get; }
    public double S1 { get; }
    public double S2 { get; }

    public ShellStress(double sx, double sy, double sxy, double s1, double s2)
    {
        Sx = sx;
        Sy = sy;
        Sxy = sxy;
        S1 = s1;
        S2 = s2;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["sx"] = Sx,
        ["sy"] = Sy,
        ["sxy"] = Sxy,
        ["s1"] = S1,
        ["s2"] = S2
    };
}

public sealed class BeamStress : QtModelRecord
{
    public double TopLeft { get; }
    public double TopRight { get; }
    public double BotLeft { get; }
    public double BotRight { get; }
    public double Sfx { get; }
    public double SmzLeft { get; }
    public double SmzRight { get; }
    public double SmyTop { get; }
    public double SmyBot { get; }

    public BeamStress(IReadOnlyList<double> values)
    {
        if (values == null || values.Count != 9)
        {
            throw new ArgumentException("操作错误:  单元应力列表有误", nameof(values));
        }

        TopLeft = values[0];
        TopRight = values[1];
        BotLeft = values[2];
        BotRight = values[3];
        Sfx = values[4];
        SmzLeft = values[5];
        SmzRight = values[6];
        SmyTop = values[7];
        SmyBot = values[8];
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["top_left"] = TopLeft,
        ["top_right"] = TopRight,
        ["bot_left"] = BotLeft,
        ["bot_right"] = BotRight,
        ["sfx"] = Sfx,
        ["smz_left"] = SmzLeft,
        ["smz_right"] = SmzRight,
        ["smy_top"] = SmyTop,
        ["smy_bot"] = SmyBot
    };
}

public sealed class ElasticLinkForce : QtModelRecord
{
    public int LinkId { get; }
    public Force Force { get; }

    public ElasticLinkForce(int linkId, IEnumerable<double> force)
    {
        var list = force?.ToArray() ?? throw new ArgumentNullException(nameof(force));
        if (list.Length != 6)
        {
            throw new ArgumentException("操作错误: 'force' 列表有误", nameof(force));
        }

        LinkId = linkId;
        Force = new Force(list[0], list[1], list[2], list[3], list[4], list[5]);
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["link_id"] = LinkId,
        ["force"] = Force.ToDictionary()
    };
}

public sealed class ConstrainEquationForce : QtModelRecord
{
    public int EquationId { get; }
    public Force Force { get; }

    public ConstrainEquationForce(int equationId, IEnumerable<double> force)
    {
        var list = force?.ToArray() ?? throw new ArgumentNullException(nameof(force));
        if (list.Length != 6)
        {
            throw new ArgumentException("操作错误: 'force' 列表有误", nameof(force));
        }

        EquationId = equationId;
        Force = new Force(list[0], list[1], list[2], list[3], list[4], list[5]);
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["equation_id"] = EquationId,
        ["force"] = Force.ToDictionary()
    };
}

public sealed class CableLengthResult : QtModelRecord
{
    public int ElementId { get; }
    public double UnstressedLength { get; }
    public double CosAxi { get; }
    public double CosAyi { get; }
    public double CosAzi { get; }
    public double CosAxj { get; }
    public double CosAyj { get; }
    public double CosAzj { get; }
    public double Dx { get; }
    public double Dy { get; }
    public double Dz { get; }

    public CableLengthResult(
        int elementId,
        double unstressedLength,
        double cosAxi = 0,
        double cosAyi = 0,
        double cosAzi = 0,
        double cosAxj = 0,
        double cosAyj = 0,
        double cosAzj = 0,
        double dx = 0,
        double dy = 0,
        double dz = 0)
    {
        ElementId = elementId;
        UnstressedLength = unstressedLength;
        CosAxi = cosAxi;
        CosAyi = cosAyi;
        CosAzi = cosAzi;
        CosAxj = cosAxj;
        CosAyj = cosAyj;
        CosAzj = cosAzj;
        Dx = dx;
        Dy = dy;
        Dz = dz;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["unstressed_length"] = UnstressedLength,
        ["cos_a_xi"] = CosAxi,
        ["cos_a_yi"] = CosAyi,
        ["cos_a_zi"] = CosAzi,
        ["cos_a_xj"] = CosAxj,
        ["cos_a_yj"] = CosAyj,
        ["cos_a_zj"] = CosAzj,
        ["dx"] = Dx,
        ["dy"] = Dy,
        ["dz"] = Dz
    };
}

public sealed class FreeVibrationResult : QtModelRecord
{
    public int Mode { get; }
    public double AngelFrequency { get; }
    public double EngineeringFrequency { get; }
    public IReadOnlyList<double> ParticipateMass { get; }
    public IReadOnlyList<double> SumParticipateMass { get; }
    public IReadOnlyList<double> ParticipateFactor { get; }

    public FreeVibrationResult(
        int mode,
        double angelFrequency,
        IEnumerable<double> participateMass,
        IEnumerable<double> sumParticipateMass,
        IEnumerable<double> participateFactor)
    {
        Mode = mode;
        AngelFrequency = angelFrequency;
        EngineeringFrequency = angelFrequency * 0.159;
        ParticipateMass = participateMass?.ToArray() ?? Array.Empty<double>();
        SumParticipateMass = sumParticipateMass?.ToArray() ?? Array.Empty<double>();
        ParticipateFactor = participateFactor?.ToArray() ?? Array.Empty<double>();
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["mode"] = Mode,
        ["angel_frequency"] = AngelFrequency,
        ["engineering_frequency"] = EngineeringFrequency,
        ["participate_mass"] = ParticipateMass,
        ["sum_participate_mass"] = SumParticipateMass,
        ["participate_factor"] = ParticipateFactor
    };
}

public sealed class ElasticBucklingResult : QtModelRecord
{
    public int Mode { get; }
    public double Eigenvalue { get; }

    public ElasticBucklingResult(int mode, double eigenvalue)
    {
        Mode = mode;
        Eigenvalue = eigenvalue;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["mode"] = Mode,
        ["eigenvalue"] = Eigenvalue
    };
}

public sealed class TendonLossResult : QtModelRecord
{
    public string TendonName { get; }
    public int BeamId { get; }
    public object Position { get; }
    public double EffectiveStress { get; }
    public double InstantStress { get; }
    public double ExceptInstantStress { get; }
    public double Ratio { get; }

    public TendonLossResult(string tendonName, int beamId, object position, double effectiveStress, double instantStress, double exceptStress)
    {
        TendonName = tendonName;
        BeamId = beamId;
        Position = position;
        EffectiveStress = effectiveStress;
        InstantStress = instantStress;
        ExceptInstantStress = exceptStress;
        Ratio = Math.Abs(instantStress) > double.Epsilon ? effectiveStress / instantStress : 0.0;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["tendon_name"] = TendonName,
        ["beam_id"] = BeamId,
        ["position"] = Position,
        ["effective_s"] = EffectiveStress,
        ["instance_s"] = InstantStress,
        ["except_s"] = ExceptInstantStress,
        ["ratio"] = Ratio
    };
}

public sealed class TendonLengthResult : QtModelRecord
{
    public string TendonName { get; }
    public int StartStage { get; }
    public double StressLength { get; }
    public double UnStressLength { get; }
    public double EffectiveStressI { get; }
    public double EffectiveStressJ { get; }
    public double ElongationI { get; }
    public double ElongationJ { get; }
    public double Elongation { get; }

    public TendonLengthResult(
        string tendonName,
        int startStage,
        double stressLength,
        double unStressLength,
        double effectStressI,
        double effectStressJ,
        double elongationI,
        double elongationJ,
        double elongation)
    {
        TendonName = tendonName;
        StartStage = startStage;
        StressLength = stressLength;
        UnStressLength = unStressLength;
        EffectiveStressI = effectStressI;
        EffectiveStressJ = effectStressJ;
        ElongationI = elongationI;
        ElongationJ = elongationJ;
        Elongation = elongation;
    }

    public override Dictionary<string, object?> ToDictionary() => new()
    {
        ["tendon_name"] = TendonName,
        ["start_stage"] = StartStage,
        ["stress_length"] = StressLength,
        ["un_stress_length"] = UnStressLength,
        ["effect_stress_i"] = EffectiveStressI,
        ["effect_stress_j"] = EffectiveStressJ,
        ["elongation_i"] = ElongationI,
        ["elongation_j"] = ElongationJ,
        ["elongation"] = Elongation
    };
}
