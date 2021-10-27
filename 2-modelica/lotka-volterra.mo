model lotkevolterra
  Modelica.Blocks.Sources.Constant delta(k = 0.2)  annotation(
    Placement(visible = true, transformation(origin = {-70, -86}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant gamma(k = 0.2)  annotation(
    Placement(visible = true, transformation(origin = {-70, -50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant alpha(k = 1.5)  annotation(
    Placement(visible = true, transformation(origin = {-70, 90}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant beta(k = 0.7)  annotation(
    Placement(visible = true, transformation(origin = {-70, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Add add(k2 = -1)  annotation(
    Placement(visible = true, transformation(origin = {36, 60}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Product product annotation(
    Placement(visible = true, transformation(origin = {-8, 84}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.MultiProduct multiProduct(nu = 3)  annotation(
    Placement(visible = true, transformation(origin = {-2, 34}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
  Modelica.Blocks.Math.Product product1 annotation(
    Placement(visible = true, transformation(origin = {-2, -50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.MultiProduct multiProduct1(nu = 3) annotation(
    Placement(visible = true, transformation(origin = {16, -24}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
  Modelica.Blocks.Math.Add add1(k2 = -1) annotation(
    Placement(visible = true, transformation(origin = {54, -38}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Continuous.Integrator integrator(y_start = 10)  annotation(
    Placement(visible = true, transformation(origin = {78, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Continuous.Integrator integrator1(y_start = 10)  annotation(
    Placement(visible = true, transformation(origin = {-68, 4}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(alpha.y, product.u1) annotation(
    Line(points = {{-58, 90}, {-20, 90}}, color = {0, 0, 127}));
  connect(beta.y, multiProduct.u[1]) annotation(
    Line(points = {{-58, 50}, {-8, 50}, {-8, 34}}, color = {0, 0, 127}));
  connect(multiProduct.y, add.u2) annotation(
    Line(points = {{5, 34}, {24, 34}, {24, 54}}, color = {0, 0, 127}));
  connect(product.y, add.u1) annotation(
    Line(points = {{4, 84}, {24, 84}, {24, 66}}, color = {0, 0, 127}));
  connect(gamma.y, product1.u2) annotation(
    Line(points = {{-58, -50}, {-46, -50}, {-46, -56}, {-14, -56}}, color = {0, 0, 127}));
  connect(product1.y, add1.u2) annotation(
    Line(points = {{10, -50}, {42, -50}, {42, -44}}, color = {0, 0, 127}));
  connect(multiProduct1.y, add1.u1) annotation(
    Line(points = {{23, -24}, {42.5, -24}, {42.5, -32}, {42, -32}}, color = {0, 0, 127}));
  connect(add.y, integrator.u) annotation(
    Line(points = {{48, 60}, {59, 60}, {59, 50}, {66, 50}}, color = {0, 0, 127}));
  connect(delta.y, multiProduct1.u[1]) annotation(
    Line(points = {{-58, -86}, {-20, -86}, {-20, -24}, {10, -24}}, color = {0, 0, 127}));
  connect(integrator1.y, multiProduct1.u[2]) annotation(
    Line(points = {{-57, 4}, {0, 4}, {0, -24}, {10, -24}}, color = {0, 0, 127}));
  connect(integrator1.y, product1.u1) annotation(
    Line(points = {{-57, 4}, {-32, 4}, {-32, -44}, {-14, -44}}, color = {0, 0, 127}));
  connect(integrator1.y, multiProduct.u[2]) annotation(
    Line(points = {{-57, 4}, {112, 4}, {112, 20}, {-16, 20}, {-16, 34}, {-8, 34}}, color = {0, 0, 127}));
  connect(integrator.y, multiProduct1.u[3]) annotation(
    Line(points = {{89, 50}, {106, 50}, {106, 10}, {-6, 10}, {-6, -18}, {10, -18}, {10, -24}}, color = {0, 0, 127}));
  connect(integrator.y, multiProduct.u[3]) annotation(
    Line(points = {{89, 50}, {96, 50}, {96, 24}, {-30, 24}, {-30, 34}, {-8, 34}}, color = {0, 0, 127}));
  connect(integrator.y, product.u2) annotation(
    Line(points = {{89, 50}, {90, 50}, {90, 72}, {-42, 72}, {-42, 78}, {-20, 78}}, color = {0, 0, 127}));
  connect(add1.y, integrator1.u) annotation(
    Line(points = {{66, -38}, {72, -38}, {72, -12}, {-90, -12}, {-90, 4}, {-80, 4}}, color = {0, 0, 127}));
  annotation(
    uses(Modelica(version = "3.2.3")));
end lotkevolterra;