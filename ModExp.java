public class ModExp {
	
	public static void main(String[] args) {
		// equation is of the form b^p%m
		int b = 23;
		int p = 376;
		int m = 37;
		
		int[] binaryExpansion = binaryExpansion(p);
		int x = 1;
		int power = b % m;
		for(int i = 0; i < binaryExpansion.length; i++) {
			if(binaryExpansion[i] == 1)
				x = (x * power) % m;
			power = (power * power) % m;
		}
		
		System.out.println(x);
	}
	
	public static int[] binaryExpansion(int number) {
		int[] out = new int[100];
		int n = 0;
		while(number > 0) {
			int mod = number % 2;
			number = number / 2 + mod;
			out[n] = mod;
			n++;
			number /= 2;
		}
		
		int[] realOut = new int[n];
		for(int i = 0; i < n; i++) {
			realOut[i] = out[i];
		}
		
		return out;
	}
	
}
