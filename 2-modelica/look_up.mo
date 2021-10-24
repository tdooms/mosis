model LookUp
  output Modelica.Blocks.Interfaces.RealOutput v_ideal(start = 0) annotation(
    Placement(visible = true, transformation(origin = {110, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {110, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  v_ideal = if time < 10 then 0 elseif time < 170 then 10
   elseif time < 200 then 8
   elseif time < 260 then 18 else 12;
  annotation(
    experiment(StopTime = 300));
end LookUp;