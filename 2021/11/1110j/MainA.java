import java.io.*;
import java.util.*;

public class MainA {
    
    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./20364.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int K = Integer.parseInt(s[0]);
		int N = Integer.parseInt(s[1]);
		HashSet<Integer> set = new HashSet<>();

		for(int z = 0; z < N;z++) {
			int cur = Integer.parseInt(br.readLine());
			int t = cur;
			int temp = 0;

			while(true) {
				if(t==0) break;
				if(set.contains(t)) temp=t;
				t/=2;
			}
			System.out.println(temp);
			if (temp==0) {
				set.add(cur);
			}
		}
    }
}
