import java.util.*;
public class learn{
    public static void main (String args[]){
        System.out.println("Hello");
        Date today = new Date();
        System.out.println(today);
        int [] numbers = {1,2,3,4,5,6,7};
         System.out.println(Arrays.toString(numbers));
         int [] numbers1 = {199,9358,9452,52935};
         Arrays.sort(numbers1);
         System.out.println(Arrays.toString(numbers1));
        int [] [] dimen = new int [3] [3];
        dimen [0] [0] = 1;
        System.out.println(Arrays.deepToString(dimen));

    }
    }
