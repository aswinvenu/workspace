/* RSA algorithm implementation */

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>

typedef unsigned char bool;
static const bool false = 0;
static const bool true = 1;

struct public_keys{
    unsigned long n;
    unsigned long e;
};

struct private_keys{
    unsigned long n;
    unsigned long d;
};

/* Recursive function to return gcd of a and b */
static int gcd(int a, int b)
{
        if (a == b)
            return a;
        if (a > b)
            return gcd(a-b, b);
        return gcd(a, b-a);
}

/* Function to return LCM of two numbers */
static int lcm(int a, int b)
{
        return (a*b)/gcd(a, b);
}
 
/* Sieve of Sundaram generating prime numbers*/
static void generate_prime(unsigned long num, unsigned long* p, unsigned long* q)
{
	/* Sieve of sundaram calculates all the prime numbers
	 * less than 2*n-1 for the given number n
	 */
	unsigned long new_n = (num-1)/2;
	unsigned long primes[100] = {};

        memset(primes, 0, sizeof(primes));

	/* Create a buffer of new_n+1 values */
	bool mark[new_n + 1];
	
	/* set all the values to be flase */
	memset(mark, false, sizeof(mark));
	
	for(unsigned long i = 1; i <= new_n; i++){
		for(unsigned long j = i; (i+j+2*i*j) < new_n; j++){
			mark[i+j+2*i*j] = true;
		}
	}

    
	/* Sieve of Sundaram starts with number 3. So we need to 
	 * manually include number 2
	 */

        unsigned long count = 0;

	if(num > 2){
                primes[0] = (unsigned long)2;
                count += 1;
	}
	
	/* All the prime numbers are flaged false */

       
	for(unsigned long i = 1; i <= new_n; i ++){
		if(mark[i] == false){
                        primes[count] = 2*i+1;
                        count += 1;
		}
	}

    
        *p = primes[rand()%count];
        *q = primes[rand()%count];
        

} 

static unsigned long generate_private_key(unsigned long pub_key, unsigned long lambda)
{
    unsigned long d = 1;

    while((d*pub_key)%lambda != 1){
        d += 1;
    }

    printf(" The pvt key is %lu ", d);
    return d;
}

static unsigned long generate_public_key(unsigned long p, unsigned long q, unsigned long* lambda)
{
    /* calculating the lambda function */
    int e;
    int random = 0;
    e = lcm((int)p-1,(int)q-1);
    *lambda = e;

    do{
        random = rand()%e;
    }while(random%e == 0);
    
    printf("prime = %d and public_key is %d \n", e, random);
    return (unsigned long) random; 
}

static void encrypt_data()
{

}

int main(void)
{   
        unsigned long p;
        unsigned long q;

        struct public_keys public_key; 
        struct private_keys private_key;
        
        unsigned long lambda;

        srand(time(NULL));

	/* function to calcule prime number and returns two prime numbers */
        generate_prime(200, &p, &q);
        
        public_key.n = private_key.n = (p*q);

        /* generate public key */
        public_key.e = generate_public_key(p, q, &lambda);
      
        /* Generating the private key */
        private_key.d = generate_private_key(public_key.e,lambda);
        
        printf(" %lu, %lu", p, q);
        return 0;
}

