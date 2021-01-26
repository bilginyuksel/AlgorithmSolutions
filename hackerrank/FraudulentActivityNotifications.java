package hackerrank;

public class FraudulentActivityNotifications {

    static int activityNotifications(int [] expenditures, int d) {
        int [] freqTable = new int[201];
        for(int i=0; i<d; i++) freqTable[expenditures[i]]++;
        int notifications = 0;

        for(int i=d; i<expenditures.length; i++) {
            int median = getMedian(freqTable, d);
            notifications += (expenditures[i] >= median)?1:0;
            freqTable[expenditures[i-d]]--;
            freqTable[expenditures[i]]++;
        }

        return notifications;
    }

    static int getMedian(int []freqTable, int d) {
        int idx1 = d/2, idx2 = (d-1)/2;
        int val1 = -1, val2 = -1;

        int count = 0;
        for(int i=0; i<freqTable.length; i++) {
            count += freqTable[i];
            if(count > idx1 && val1 == -1) {
                val1 = i;
            }
            if(count > idx2 && val2 == -1) {
                val2 = i;
            }
            if(val1 != -1 && val2 != -1) return val1+val2;
        }

        return -1;
    }
}

