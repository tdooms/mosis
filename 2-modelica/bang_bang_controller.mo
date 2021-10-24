model BangBangController

  parameter Real d_min(start = 0);
  parameter Real d_max(start = 0);
  parameter Real g(start = 0);
  
  Boolean active(start = false, fixed=true);
  
  input Modelica.Blocks.Interfaces.RealInput u(start = 0) annotation(
    Placement(visible = true, transformation(origin = {-100, 0}, extent = {{-20, -20}, {20, 20}}, rotation = 0), iconTransformation(origin = {-120, 0}, extent = {{-20, -20}, {20, 20}}, rotation = 0)));
  
  output Modelica.Blocks.Interfaces.RealOutput F(start = 0) annotation(
    Placement(visible = true, transformation(origin = {100, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {110, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));

equation
  active = if u > d_max then true elseif u < d_min then false else pre(active);
  F = if active then g else 0;

end BangBangController;