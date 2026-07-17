public class methodoverloading{
    public static void main (String args[]){
        calc(" ABI ",30);
        calc(40);
    }
    public static int calc(String playername , int score){
        System.out.println(" Player "  + playername + " score " + score);
        return score;

    }
        public static int calc(int score){
        System.out.println(" Player is unknown " + " score " + score);
        return score;

    }
}