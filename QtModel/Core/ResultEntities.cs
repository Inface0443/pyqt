using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;

namespace QtModel.Core;

public record NodeDisplacement(int NodeId, IReadOnlyList<double> Displacements, double Time = 0)
{
    public double Dx => Displacements.ElementAtOrDefault(0);
    public double Dy => Displacements.ElementAtOrDefault(1);
    public double Dz => Displacements.ElementAtOrDefault(2);
    public double Rx => Displacements.ElementAtOrDefault(3);
    public double Ry => Displacements.ElementAtOrDefault(4);
    public double Rz => Displacements.ElementAtOrDefault(5);

    public Dictionary<string, object> ToDictionary() => new()
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

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record SupportReaction(int NodeId, IReadOnlyList<double> Force, double Time = 0)
{
    public double Fx => Force.ElementAtOrDefault(0);
    public double Fy => Force.ElementAtOrDefault(1);
    public double Fz => Force.ElementAtOrDefault(2);
    public double Mx => Force.ElementAtOrDefault(3);
    public double My => Force.ElementAtOrDefault(4);
    public double Mz => Force.ElementAtOrDefault(5);

    public Dictionary<string, object> ToDictionary() => new()
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

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record BeamElementForce(int ElementId, Force ForceI, Force ForceJ, double Time = 0)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["time"] = Time,
        ["force_i"] = ForceI.ToDictionary(),
        ["force_j"] = ForceJ.ToDictionary()
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record TrussElementForce(int ElementId, IReadOnlyList<double> ForceI, IReadOnlyList<double> ForceJ, double Time = 0)
{
    public double Ni => ForceI.ElementAtOrDefault(3);
    public double Fxi => ForceI.ElementAtOrDefault(0);
    public double Fyi => ForceI.ElementAtOrDefault(1);
    public double Fzi => ForceI.ElementAtOrDefault(2);
    public double Nj => ForceJ.ElementAtOrDefault(3);
    public double Fxj => ForceJ.ElementAtOrDefault(0);
    public double Fyj => ForceJ.ElementAtOrDefault(1);
    public double Fzj => ForceJ.ElementAtOrDefault(2);

    public Dictionary<string, object> ToDictionary() => new()
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

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record ShellElementForce(int ElementId, IReadOnlyList<double> Force, double Time = 0)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["time"] = Time,
        ["force"] = Force
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record CompositeElementForce(int ElementId, IReadOnlyList<double> Force, double Time = 0)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["time"] = Time,
        ["force"] = Force
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record BeamElementStress(int ElementId, BeamStress StressI, BeamStress StressJ, double Time = 0)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["time"] = Time,
        ["stress_i"] = StressI.ToDictionary(),
        ["stress_j"] = StressJ.ToDictionary()
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record ShellElementStress(int ElementId, ShellStress StressI, ShellStress StressJ, double Time = 0)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["time"] = Time,
        ["stress_i"] = StressI.ToDictionary(),
        ["stress_j"] = StressJ.ToDictionary()
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record TrussElementStress(int ElementId, IReadOnlyList<double> StressI, IReadOnlyList<double> StressJ, double Time = 0)
{
    public double Ni => StressI.ElementAtOrDefault(3);
    public double Fxi => StressI.ElementAtOrDefault(0);
    public double Fyi => StressI.ElementAtOrDefault(1);
    public double Fzi => StressI.ElementAtOrDefault(2);
    public double Nj => StressJ.ElementAtOrDefault(3);
    public double Fxj => StressJ.ElementAtOrDefault(0);
    public double Fyj => StressJ.ElementAtOrDefault(1);
    public double Fzj => StressJ.ElementAtOrDefault(2);

    public Dictionary<string, object> ToDictionary() => new()
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

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record CompositeBeamStress(int ElementId, IReadOnlyList<double> Stress, double Time = 0)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["time"] = Time,
        ["stress"] = Stress
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record Force(double Fx, double Fy, double Fz, double Mx, double My, double Mz)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["Fx"] = Fx,
        ["Fy"] = Fy,
        ["Fz"] = Fz,
        ["Mx"] = Mx,
        ["My"] = My,
        ["Mz"] = Mz
    };
}

public record ShellStress(double Nx, double Ny, double Nxy, double Mx, double My, double Mxy, double Qx, double Qy)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["Nx"] = Nx,
        ["Ny"] = Ny,
        ["Nxy"] = Nxy,
        ["Mx"] = Mx,
        ["My"] = My,
        ["Mxy"] = Mxy,
        ["Qx"] = Qx,
        ["Qy"] = Qy
    };
}

public record BeamStress(double N, double V2, double V3, double T, double M2, double M3)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["N"] = N,
        ["V2"] = V2,
        ["V3"] = V3,
        ["T"] = T,
        ["M2"] = M2,
        ["M3"] = M3
    };
}

public record ElasticLinkForce(int LinkId, IReadOnlyList<double> ForceI, IReadOnlyList<double> ForceJ, double Time = 0)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["link_id"] = LinkId,
        ["time"] = Time,
        ["force_i"] = ForceI,
        ["force_j"] = ForceJ
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record ConstrainEquationForce(int ConstraintId, IReadOnlyList<double> Force, double Time = 0)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["constraint_id"] = ConstraintId,
        ["time"] = Time,
        ["force"] = Force
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record CableLengthResult(int ElementId, double Length, double Force, double Time = 0)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["element_id"] = ElementId,
        ["time"] = Time,
        ["length"] = Length,
        ["force"] = Force
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record FreeVibrationResult(int Mode, double Frequency, double Period)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["mode"] = Mode,
        ["frequency"] = Frequency,
        ["period"] = Period
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record ElasticBucklingResult(int Mode, double LoadFactor)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["mode"] = Mode,
        ["load_factor"] = LoadFactor
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record TendonLossResult(string TendonName, double TotalLoss, IReadOnlyDictionary<string, double> LossComponents)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["tendon_name"] = TendonName,
        ["total_loss"] = TotalLoss,
        ["loss_components"] = LossComponents
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}

public record TendonLengthResult(string TendonName, double InitialLength, double FinalLength)
{
    public Dictionary<string, object> ToDictionary() => new()
    {
        ["tendon_name"] = TendonName,
        ["initial_length"] = InitialLength,
        ["final_length"] = FinalLength
    };

    public override string ToString() => JsonSerializer.Serialize(ToDictionary());
}
