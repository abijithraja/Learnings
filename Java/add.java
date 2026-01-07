import java.util.*;
class add{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter first number: ");
        int a = sc.nextInt();
        System.out.print("Enter second number: ");
        int b = sc.nextInt();
        int c = 0;
        for (int i=0; i<b; i++){
            c += a;
        }
        System.out.println("ans: "+c);
        sc.close();
    }
}