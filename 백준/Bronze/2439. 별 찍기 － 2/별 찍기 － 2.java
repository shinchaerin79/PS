import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        StringBuilder out = new StringBuilder();

        for (int i = 1; i <= N; i++) {
            // 왼쪽에 채울 공백: N - i 개
            for (int s = 0; s < N - i; s++) out.append(' ');
            // 별: i 개
            for (int star = 0; star < i; star++) out.append('*');
            out.append('\n');
        }

        System.out.print(out.toString());
    }
}
