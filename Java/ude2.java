public class ude2 {
    public static void main(String args[]){
        addition();
        int result = sub();
        System.out.println(result);
        }
    public static void addition(){
        int a = 10;
        int b = 20;
        System.out.println(a+b);
    }
    public static int sub(){
        int a = 50;
        int b = 40;
        return a-b;
    }
    }