class TimeMap {
    private Map<String, List<List<Object>>> self;

    public TimeMap() {
        self = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        ArrayList<Object> pair = new ArrayList<>();
        pair.add(value);
        pair.add(timestamp);
        if (self.get(key) == null) {
            ArrayList<List<Object>> values = new ArrayList<>();
            values.add(pair);
            self.put(key, values);
        } else {
            List<List<Object>> tempList = self.get(key);
            tempList.add(pair);
            self.put(key, tempList);
        }
    }

    public String get(String key, int timestamp) {
        if (self.get(key) == null) {
            return "";
        }
        List<List<Object>> target = self.get(key);
        int n = target.size();
        if (timestamp < (Integer) target.get(0).get(1)) {
            return "";
        }
        else if (timestamp > (Integer) target.get(n-1).get(1)) {
            return (String) target.get(n-1).get(0);
        }
        else {
            int left = 0;
            int right = n - 1;
            while (left < right) {
                if (timestamp == (Integer) target.get(left).get(1)) {
                    return (String) target.get(left).get(0);
                }
                else if (timestamp == (Integer) target.get(right).get(1)) {
                    return (String) target.get(right).get(0);
                }
                else {
                    int middle = left + (right - left)/2;
                    if (timestamp == (Integer) target.get(middle).get(1)) {
                        return (String) target.get(middle).get(0);
                    }
                    else if (timestamp > (Integer) target.get(middle).get(1)) {
                        left = middle + 1;
                    }
                    else {
                        right = middle - 1;
                    }
                }
            }

            if (timestamp < (Integer) target.get(right).get(1)) {
                return (String) target.get(right - 1).get(0);
            }
            return (String) target.get(right).get(0);
        }

        
    }
}
