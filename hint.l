%{
#include <iostream> 
using namespace std;
int no_lines = 0; 
%}

%option noyywrap	

%%
[ \t];
\n    			{no_lines++;}
"call"          {cout   << "< " << no_lines + 1   << ", Keyword, " << yytext << '>' << endl;}
"cancel"        {cout   << "< " << no_lines + 1   << ", Keyword, " << yytext << '>' << endl;}
[1-3]{4}	    {cout   << "< " << no_lines + 1   << ", Const, "   << yytext << '>' << endl;}
.               {/*cout << "<Unknown, " << yytext << '>' << endl;*/}
%%		

int main(int argc, char** argv)
{
    yylex();
    return 0;
}
