import java.util.*;
public class Palindrome {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter any string: ");
        String sample = sc.nextLine();
        boolean isPalindrome = true;
        for (int i = 0; i < sample.length() / 2; i++) {
            if (sample.charAt(i) != sample.charAt(sample.length() - 1 - i)) {
                isPalindrome = false;
                break;
            }
        }
        if (isPalindrome) {
            System.out.println("It is a palindrome.");
        } else {
            System.out.println("It is not a palindrome.");
        }
        sc.close();
    }
}