import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();

        int total = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c >= 'A' && c <= 'C') total += 3;
            else if (c >= 'D' && c <= 'F') total += 4;
            else if (c >= 'G' && c <= 'I') total += 5;
            else if (c >= 'J' && c <= 'L') total += 6;
            else if (c >= 'M' && c <= 'O') total += 7;
            else if (c >= 'P' && c <= 'S') total += 8;
            else if (c >= 'T' && c <= 'V') total += 9;
            else total += 10;
        }
        System.out.println(total);
    }
}