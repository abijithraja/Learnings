public class challenge {
    public static void main(String args[]){
        System.out.println("1hr in sec:"+time(1));
        System.out.println("1hr in sec:"+time(2,60));
    }
    static int time(int hr){
       int seconds=hr*3600;
        return seconds;
    }
    static int time(int hr,int min){
       int hour =hr*3600;
       int minutes=min*60;
       int seconds = hour+minutes;
       return seconds;  
}
}
