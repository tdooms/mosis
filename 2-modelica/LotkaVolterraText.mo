model LotkaVolterra
  output Real x(start=10, fixed=true);
  output Real y(start=10, fixed=true);
  parameter Real alpha=1.5;
  parameter Real beta=0.7;
  parameter Real delta=0.2;
  parameter Real gamma=0.2;
equation
  der(x) = alpha*x-beta*x*y;
  der(y) = delta*x*y-gamma*y;
end LotkaVolterra;