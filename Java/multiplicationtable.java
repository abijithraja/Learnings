import java.util.*;
class multiplicationtable{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of the table:");
        int n = sc.nextInt();
        for(int i=1;i<=10;i++){
            if (i!=5 && i!=6){
            System.out.println(n+" * "+i+" = "+(n*i));
            }
        }
    }
}