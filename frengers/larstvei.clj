(require '[clojure.set :refer [intersection]]
         '[clojure.string :refer [split]]
         '[clojure.java.io :refer [reader]])

(defn add [[friendmap met] data]
  (if (= (data 0) "friends")
    [(-> friendmap
         (update (data 1) (fnil conj #{}) (data 2))
         (update (data 2) (fnil conj #{}) (data 1))) met]
    [friendmap (conj met [(data 1) (data 2)])]))

(defn frengers [friendmap [a b]]
  (and (<= 3 (count (intersection (friendmap a) (friendmap b))))
       (not ((fnil (friendmap a) #{}) b))))

(let [data (map #(split % #" ") (line-seq (reader *in*)))
      [friendmap met] (reduce add [{} #{}] data)]
  (-> (filter (partial frengers friendmap) met) count println))
