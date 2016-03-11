(require '[clojure.string :refer [split]]
         '[clojure.java.io :refer [reader]])

(defn add [[friends hatemap] data]
  (if (= (data 0) "friends")
    [(conj friends (vec (rest data))) hatemap]
    [friends (update hatemap (data 0) (fnil conj #{}) (data 2))]))

(defn frenemies [hatemap [a b]]
  (and ((fnil (hatemap a) #{}) b) ((fnil (hatemap b) #{}) a)))

(let [data (map #(split % #" ") (line-seq (reader *in*)))
      [friends hatemap] (reduce add [#{} {}] data)]
  (-> (filter (partial frenemies hatemap) friends) count println))
