import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] basket = new int[N + 1];

        for (int t = 0; t < M; t++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            for (int idx = i; idx <= j; idx++) {
                basket[idx] = k;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int idx = 1; idx <= N; idx++) {
            sb.append(basket[idx]);
            if (idx < N) sb.append(' ');
        }

        System.out.print(sb.toString());
    }
}
