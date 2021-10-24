model PRT_system
  Modelica.Blocks.Math.Product product annotation(
    Placement(visible = true, transformation(origin = {-10, 30}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  Modelica.Blocks.Sources.Constant negative(k = -1)  annotation(
    Placement(visible = true, transformation(origin = {50, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  Modelica.Blocks.Math.MultiSum multiSum(nu = 2) annotation(
    Placement(visible = true, transformation(origin = {-4, -30}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
  LookUp lookUp annotation(
    Placement(visible = true, transformation(origin = {-50, -30}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  CustomPlant customPlant annotation(
    Placement(visible = true, transformation(origin = {50, 10}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  BangBangController bangBangController annotation(
    Placement(visible = true, transformation(origin = {30, -30}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(negative.y, product.u2) annotation(
    Line(points = {{39, 50}, {2, 50}, {2, 36}}, color = {0, 0, 127}));
  connect(product.y, multiSum.u[1]) annotation(
    Line(points = {{-21, 30}, {-31, 30}, {-31, -26.875}, {-11, -26.875}, {-11, -30}}, color = {0, 0, 127}));
  connect(lookUp.v_ideal, multiSum.u[2]) annotation(
    Line(points = {{-39, -30}, {-7, -30}}, color = {0, 0, 127}));
  connect(bangBangController.F, customPlant.F_traction) annotation(
    Line(points = {{41, -30}, {68, -30}, {68, 10}, {62, 10}}, color = {0, 0, 127}));
  connect(customPlant.x_psgr, product.u1) annotation(
    Line(points = {{39, 15}, {24, 15}, {24, 24}, {2, 24}}, color = {0, 0, 127}));
  connect(multiSum.y, bangBangController.u) annotation(
    Line(points = {{3.02, -30}, {18, -30}}, color = {0, 0, 127}));
  annotation(
    experiment(StopTime = 300),
    uses(Modelica(version = "3.2.3")));
end PRT_system;