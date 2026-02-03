public class activeuser {
    static void rec(int i){
        if (i==10){
            return;
        }
        System.out.println(i);
       rec(i+1);
    }
    
    static void rec2(int i){
        if (i==17){
            return;
        }
        System.out.println(i);
       rec2(i+2);
    }
    
    public static void main(String[] args) {
        rec(1);
        rec2(2);
        
    }
}
    

