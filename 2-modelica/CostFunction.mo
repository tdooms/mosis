model CostFunction
  Real cost(start=0);
  Modelica.Blocks.Interfaces.RealInput v_ideal(start=0) annotation(
    Placement(visible = true, transformation(origin = {-120, 0}, extent = {{-20, -20}, {20, 20}}, rotation = 0), iconTransformation(origin = {-120, 0}, extent = {{-20, -20}, {20, 20}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealInput x_psgr(start=0) annotation(
    Placement(visible = true, transformation(origin = {-120, -60}, extent = {{-20, -20}, {20, 20}}, rotation = 0), iconTransformation(origin = {-120, -60}, extent = {{-20, -20}, {20, 20}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealInput v_trolley(start=0) annotation(
    Placement(visible = true, transformation(origin = {-120, 60}, extent = {{-20, -20}, {20, 20}}, rotation = 0), iconTransformation(origin = {-120, 60}, extent = {{-20, -20}, {20, 20}}, rotation = 0)));
equation

cost = if abs(x_psgr) < 0.35 then (v_ideal - v_trolley)^2 else 10000000000;

annotation(
    uses(Modelica(version = "3.2.3")));
end CostFunction;