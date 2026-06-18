class Solution {

    public String encode(List<String> strs) {
        String str = "";
        for(int i = 0; i < strs.size(); i++) {
            str+=String.valueOf(strs.get(i).length())+'#'+strs.get(i);
        }
        return str;

    }

    public List<String> decode(String str) {
        int i = 0;
        ArrayList<String> newList = new ArrayList<>();
        while(i<str.length()) {
            int j = i;
            while(str.charAt(j)!='#') {
                j++;
            }
            int length = Integer.parseInt(str.substring(i,j));

            String s = str.substring(j+1,j+1+length);
            newList.add(s);
            i = j + 1 + length;
        }
        return newList;

    }
}
