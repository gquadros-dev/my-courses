void main() {

  int age = 16; // poderia ser colocado como "var", assim vira tipagem dinâmica
  double height = 1.76;
  bool geek = true; // pode fazer comparações como "bool geek = (age == height)"
  const String name = 'Gabriel Quadros';
  const String nick = 'Gabe';
  final bool maiorDeIdade;
  int energia = 100;

  if(age >= 18){ // mesma coisa que em JS
    maiorDeIdade = true;
  } else { // mesma coisa que em JS
    maiorDeIdade = false;
  }

  // for(int i = 1; i < 59; i++){ // mesma coisa que o for em JS
  //   print('EU RODEI $i vezes');
  // }

  while (energia>0){
    print('Mais uma repetição!');
    energia -= 6;
  }

  // do{
  //   print('Mais uma repetição!');
  //   energia -= 6;
  // } while(energia>0);

  // List<String> namelist = ['Ricardo', 'Gabriel', 'Mauricio', 'Roberto', 'Evaldo'];
  List<dynamic> gabriel = [age, height, geek, name, nick];

  // print('Hello world, my name is ${gabriel[3]}, my age is ${gabriel[0]}, my height is ${gabriel[1]} and am I geek? ${gabriel[2]}! And my nickname is ${gabriel[4]}. Am I an adult? $maiorDeIdade!');
}