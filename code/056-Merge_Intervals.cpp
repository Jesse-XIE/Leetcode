// Description: 
// ---------------

// Given a collection of intervals, merge all overlapping intervals.
// For example,
// Given [1,3],[2,6],[8,10],[15,18],
// return [1,6],[8,10],[15,18].



/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
     bool compare(Interval & intv1, Interval &intv2){
    return(intv1.start < intv2.start);
}
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> results;
        if(intervals.size() == 0){
            return results;
        }
        sort(intervals.begin(), intervals.end(), compare);
        Interval new_intv(intervals[0].start, intervals[0].end);
        int size;
        size = intervals.size();
        for (int i = 1; i != size; ++i){
            if(new_intv.end < intervals[i].start){
                results.push_back(new_intv);
                new_intv.start = intervals[i].start;
                new_intv.end = intervals[i].end;
            }
            else{
                new_intv.end = max(new_intv.end, intervals[i].end);
            }
        }
        results.push_back(new_intv);
        return results;
    }
};