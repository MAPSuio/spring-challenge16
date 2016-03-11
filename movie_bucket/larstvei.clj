(require '[clojure.string :refer [split]]
         '[clojure.java.io :refer [reader]])

(defn operate [movies [op movie]]
  (case op
    "buys" (conj movies movie)
    "watches" (conj (remove #{movie} movies) movie)
    "sells" (remove #{movie} movies)))

(let [data (map #(split % #" " 2) (line-seq (reader *in*)))
      movies (reduce operate () data)]
  (println (inc (.indexOf movies "Gone with the Wind"))))
