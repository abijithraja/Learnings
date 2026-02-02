public class activeuser {
    static void rec(int i){
        if (i==10){
            return;
        }
        System.out.println(i);
       rec(i+1);
    }
    public static void main(String[] args) {
        rec(1);
        
    }
    
}
