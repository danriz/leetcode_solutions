const gridTraveller = (m,n, memo={})=>
{
    console.dir(memo)
const key = m+','+n;    
const key2 = n+','+m;
if (key in memo) return memo[key];
if (key2 in memo) return memo[key2];
if (m==1 && n==1) return 1;
if (m==0 || n==0) return 0;

memo[key]=gridTraveller(m-1,n,memo)+gridTraveller(m,n-1,memo);
return memo[key];
};

console.log(gridTraveller(3,3));
