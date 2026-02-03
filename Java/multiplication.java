import java.util.*;
public class multiplication {
    
    static int powerOfFour(int a, int power) {
        return a << (2 * power);  
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        System.out.print("Enter power of 4: ");
        int pow = sc.nextInt();
        int result = powerOfFour(num, pow);
        System.out.println(num + " x 4^" + pow + " = " + result);
    }
}
