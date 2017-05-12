import java.util.Scanner;

public class Main {
  
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.print("Type in your name: ");
        String name=sc.nextLine();
        System.out.print("Type in your age: ");
        int age = sc.nextInt();
        
        
      
        if(age <= 0) {
            System.out.println("Please "+ name + ", type a valid age.");
        } else if(age <= 16) {
            System.out.println("Sorry "+ name +". You're too young.");
        } else if(age <= 100) {
            System.out.println("Welcome, "+ name +"!");
        } else {
            System.out.println("Really, "+ name + "? Are you really "+ age + " years old?");
        }
    }
}
