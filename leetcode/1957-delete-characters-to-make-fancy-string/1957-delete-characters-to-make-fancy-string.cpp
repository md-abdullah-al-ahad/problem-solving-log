class Solution
{
public:
    string makeFancyString(string s)
    {
        int n = s.size();
        string s1 = "";
        s1 += s[0];
        int currentequal = 1;
        for (int i = 1; i < n; i++)
        {
            if (s[i] == s[i - 1])
            {
                currentequal++;
            }
            else
            {
                currentequal = 1;
            }
            if (currentequal < 3)
            {
                s1 += s[i];
            }
        }
        return s1;
    }
};