(defn sorting-dimonds [n]
  (letfn [(move [deck]
            (when (not-empty deck)
              (into [(peek deck)] (pop deck))))
          (step [deck card] (into [card] (move deck)))]
    (reduce step [] (range n 0 -1))))
