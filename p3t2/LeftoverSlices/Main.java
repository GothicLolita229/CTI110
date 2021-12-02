import java.util.Scanner;
class Main {
  public static void main(String[] args) {
  
      //Variables
      Integer pizzas, slicesPerPizza, totalSlices, people, leftover;
      final Integer SLICES_PER_PERSON = 2;
      Scanner k = new Scanner (System.in);
      //Input
      System.out.print("How many pizzas will you have? ");
      pizzas = k.nextInt();
      System.out.print("How many slices per pizza? ");
      slicesPerPizza = k.nextInt();
      System.out.print("How many people are eating pizza? ");
      people = k.nextInt();
      //Calculations
      totalSlices = pizzas * slicesPerPizza;
      leftover = totalSlices - (people * SLICES_PER_PERSON);
      //Output
      System.out.println("There will be " + leftover + " leftover slices."); 
  }
}