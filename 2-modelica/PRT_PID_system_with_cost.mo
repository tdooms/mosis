model PRT_PID_system_with_cost
  Modelica.Blocks.Math.Product product annotation(
    Placement(visible = true, transformation(origin = {-10, 30}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  Modelica.Blocks.Sources.Constant negative(k = -1)  annotation(
    Placement(visible = true, transformation(origin = {50, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  Modelica.Blocks.Math.MultiSum multiSum(nu = 2) annotation(
    Placement(visible = true, transformation(origin = {-4, -30}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
  LookUp lookUp annotation(
    Placement(visible = true, transformation(origin = {-52, -30}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  CustomPlant customPlant(A = 9.12, C_D = 0.6, c = 150, k = 300, m_psgr = 77, m_trolley = 2376, p = 1.2)  annotation(
    Placement(visible = true, transformation(origin = {50, 10}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  Modelica.Blocks.Continuous.PID pid(Td = 0.07505208070216672, Ti = 66.35465944290725, k = 329.3795484078204)  annotation(
    Placement(visible = true, transformation(origin = {56, -30}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  CostFunction costFunction annotation(
    Placement(visible = true, transformation(origin = {36, -72}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(negative.y, product.u2) annotation(
    Line(points = {{39, 50}, {2, 50}, {2, 36}}, color = {0, 0, 127}));
  connect(product.y, multiSum.u[1]) annotation(
    Line(points = {{-21, 30}, {-31, 30}, {-31, -26.875}, {-11, -26.875}, {-11, -30}}, color = {0, 0, 127}));
  connect(lookUp.v_ideal, multiSum.u[2]) annotation(
    Line(points = {{-41, -30}, {-7, -30}}, color = {0, 0, 127}));
  connect(product.u1, customPlant.v_trolley) annotation(
    Line(points = {{2, 24}, {20, 24}, {20, 5}, {40, 5}, {40, 6}}, color = {0, 0, 127}));
  connect(multiSum.y, pid.u) annotation(
    Line(points = {{4, -30}, {44, -30}}, color = {0, 0, 127}));
  connect(multiSum.y, pid.u) annotation(
    Line(points = {{4, -30}, {36, -30}}, color = {0, 0, 127}));
  connect(pid.y, customPlant.F_traction) annotation(
    Line(points = {{68, -30}, {78, -30}, {78, 10}, {62, 10}}, color = {0, 0, 127}));
  connect(customPlant.v_trolley, costFunction.v_trolley) annotation(
    Line(points = {{40, 6}, {12, 6}, {12, -66}, {24, -66}}, color = {0, 0, 127}));
  connect(customPlant.x_psgr, costFunction.x_psgr) annotation(
    Line(points = {{40, 16}, {6, 16}, {6, -78}, {24, -78}}, color = {0, 0, 127}));
  connect(lookUp.v_ideal, costFunction.v_ideal) annotation(
    Line(points = {{-40, -30}, {-22, -30}, {-22, -72}, {24, -72}}, color = {0, 0, 127}));
protected
  annotation(
    experiment(StopTime = 300),
    uses(Modelica(version = "3.2.3")));
end PRT_PID_system_with_cost;