import java.util.*;
class prob{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int[] arr={97,7,11,14,27,34,57,23,98,42,2,99};  
        int max = arr[0]; 
        for(int i=0; i<arr.length; i++){
            if(arr[i] > max){
                max = arr[i];
            }
        }
        int secondmax=0;
        for(int i=0; i<arr.length; i++){
            if(arr[i] > secondmax && arr[i] < max){
                secondmax = arr[i];
            }
        }
        System.out.println("max value is: "+max);
        System.out.println("second max value is: "+secondmax);
        sc.close();
    }
}