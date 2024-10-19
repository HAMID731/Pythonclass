import java.util.Scanner;/*Import the Scanner class from java.util package.*/


public class bodyMassindex{

public static void main(String[]args){
 /** @param args Command-line arguments.
     */
Scanner weight = new Scanner(System.in);// Reads user input from console


System.out.println("ENTER WEIGHT IN KILOGRAM");
double num1 = weight.nextDouble();// Prompt user for input weight in kilogram

System.out.println("ENTER HEIGHT IN METERS");
double num2 = weight.nextDouble();// Prompt user for input height in meters

double sum = num1/(num2*num2);// Calculate BMI (Body Mass Index)

System.out.println("the BMI(Body Mass Index) is " + sum);  // Display BMI result

}
}
