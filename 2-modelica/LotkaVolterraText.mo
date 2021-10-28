model LotkaVolterra
  parameter Real alpha=1.5;
  parameter Real beta=0.7;
  parameter Real delta=0.2;
  parameter Real gamma=0.2;
  Modelica.Blocks.Interfaces.RealOutput x(start=10, fixed=true) annotation(
    Placement(visible = true, transformation(origin = {110, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {110, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealOutput y(start=10, fixed=true) annotation(
    Placement(visible = true, transformation(origin = {110, -48}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {110, -50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  der(x) = alpha*x-beta*x*y;
  der(y) = delta*x*y-gamma*y;
annotation(
    uses(Modelica(version = "3.2.3")));
end LotkaVolterra;