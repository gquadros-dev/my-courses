void main() {

  int age = 25; // poderia ser colocado como "var", assim vira tipagem dinâmica
  double height = 1.76;
  bool geek = true; // pode fazer comparações como "bool geek = (age == height)"
  const String name = 'Gabriel Quadros';
  const String nick = 'Gabe';

  // List<String> namelist = ['Ricardo', 'Gabriel', 'Mauricio', 'Roberto', 'Evaldo'];
  List<dynamic> gabriel = [age, height, geek, name, nick];

  print('Hello world, my name is ${gabriel[3]}, my age is ${gabriel[0]}, my height is ${gabriel[1]} and am I geek? ${gabriel[2]}! And my nickname is ${gabriel[4]}.');
}