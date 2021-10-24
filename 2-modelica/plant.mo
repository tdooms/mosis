model CustomPlant
  Real v_psgr(start = 0);
  Real x_trolley(start = 0);
  
  parameter Real m_psgr(start = 1);
  parameter Real m_trolley(start = 1);
  
  parameter Real k(start = 0);
  parameter Real c(start = 0);
  parameter Real C_D(start = 0);
  parameter Real p(start = 0);
  parameter Real A(start = 0);
  
  input Modelica.Blocks.Interfaces.RealInput F_traction(start = 0) annotation(
    Placement(visible = true, transformation(origin = {-100, 0}, extent = {{-20, -20}, {20, 20}}, rotation = 0), iconTransformation(origin = {-120, 0}, extent = {{-20, -20}, {20, 20}}, rotation = 0)));
  
  output Modelica.Blocks.Interfaces.RealOutput v_trolley(start = 0) annotation(
    Placement(visible = true, transformation(origin = {110, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {110, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  output Modelica.Blocks.Interfaces.RealOutput x_psgr(start = 0) annotation(
    Placement(visible = true, transformation(origin = {110, -50}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {110, -50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation  
  der(v_psgr) = (-k * x_psgr - c * v_psgr - m_psgr * ((F_traction - .5*p*v_trolley^2*C_D*A)/(m_trolley + m_psgr)))/m_psgr;
  
  der(v_trolley) = (F_traction - .5 * p * v_trolley^2 * C_D * A) / (m_trolley + m_psgr);
  der(x_psgr) = v_psgr;
  der(x_trolley) = v_trolley;
end CustomPlant;