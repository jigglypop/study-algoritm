import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer sk = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(sk.nextToken());
        ArrayList<Integer> nums = new ArrayList<Integer>();
        for (int i = 0; i < N; i++)
            nums.add(Integer.parseInt(br.readLine()));
        Collections.sort(nums);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++)
            sb.append(nums.get(i)).append(" ");
        System.out.println(sb);
    }
}