import java.util.Scanner;/*Import the Scanner class from java.util package.*/


public class sumOfintegers{/*declaration of a class.*/

public static void main(String[]args){
/** @param args Command-line arguments.
     */
Scanner modulus= new Scanner(System.in);// Reads user input from console

System.out.println("ENTER INTEGER : ");
int num1= modulus.nextInt();// Prompt user to enter integer
int cal1= num1 % 10;//creating variables
int cal2= num1 / 10;
int rough= cal2 % 10;
int cal3= num1 /100;

int calculator= cal1 + rough + cal3;// Add the answer

System.out.println(calculator);/** print the total. */


}
}