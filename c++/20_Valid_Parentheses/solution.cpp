class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for (int i = 0; i < s.length(); i++) {
            switch(s[i]) {
                case '(':
                    stack.push_back(s[i] + 1);
                    break;
                case '{':
                case '[':
                    stack.push_back(s[i] + 2);
                    break;
                default:
                    if (stack.size() == 0 || s[i] != stack.back())
                        return false;
                    else
                        stack.pop_back();
            }
        }
        return stack.size() == 0;
    }
};
