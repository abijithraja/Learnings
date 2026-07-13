public class solution1 {
    
    public static void main(String[] args) {
        char finalDiff = diff("abcd", "abcdh"); 
        System.out.print(finalDiff); 
    }
    public static char diff(String word1, String word2) {
        char result = 0;
        for (char c : word1.toCharArray()){ 
            result ^= c;
        }
        for (char c : word2.toCharArray()) {
            result ^= c;
        }
        return result;
    }
}