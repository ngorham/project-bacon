

/**
 * bacon.js
 * Purpose: Find a path from user chosen key word and target word
 * @author Neil Gorham ngorham2@gmail.com
 * @version 1.1 12/04/2015
 */

//WordNode constructor
function WordNode(data) {
    this.word = data;
    this.next = null;
}

//bacon constructor
function Bacon(keyWord, targetWord, data) {
    //member variables
    this.keyWord = keyWord.toLowerCase(); //user key word string
    this.targetWord = new WordNode(targetWord.toLowerCase()); //user target word
    self = this;
    this.wList = []; //array of dictionary of string words
    this.container = []; //array of wordNode arrays
    this.path = []; //array of wordNodes of path from targetWord to keyWord
    this.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M', 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    this.alphabetScore = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10];
    this.searchStatus = false; //boolean of search results
    this.load(data);
    this.run();

}

Bacon.prototype = {
    constructor: Bacon,

    //load the dictionary
    load: function(data){
        for(var i = 0; i < data.length; i++)
            this.wList.push(new WordNode(data[i].trim().toLowerCase()));
    },

    //Main process
    run: function(){
        $(".bacometer").fadeOut();
        $results = $("#results");
        $('#message').html("");
        $results.html("");
        $loading = $(document.createElement('p'));
        $loading.addClass("loading animate pulse infinite");
        $results.append($loading);

        var first = []; //empty array of wordNodes
        first.push(new WordNode(this.keyWord));
        this.removeFromWordList(this.keyWord);
        this.container.push(first);
        this.searchStatus = this.search(this.container[0]);
        this.setPath();
        this.print();
    },

    //Remove word from wList
    removeFromWordList: function(word){
        for(var i = 0; i < this.wList.length; i++){
            if(this.wList[i].word == word){
                this.wList.splice(i, 1);
                break;
            }
        }
    },

    //Find adjacent words to the targetWord in wordList list
    search: function(list){
        if(typeof list == 'undefined' || list.length <= 0) return false;
        var temp = []; //empty wordNode list
        var count = 0; //count of matching characters between two words
        for(var i = 0; i < list.length; i++){ //wordNode list
            for(var j = 0; j < this.wList.length; j++){ //wordList strings
                for(var k = 0; k < list[i].word.length; k++){
                    //Compare characters between two words
                    if(list[i].word.indexOf(this.wList[j].word.charAt(k)) != -1
                        && list[i].word.charAt(k) == this.wList[j].word.charAt(k)){
                        count++; //count matching characters
                    }
                }
                if(count >= (list[i].word.length - 1)){
                    this.wList[j].next = list[i];
                    temp.push(this.wList[j]);
                    this.wList.splice(j, 1);
                }
                count = 0; //rest count
            }
        }
        if(temp.length <= 0) return false;
        this.container.push(temp);
        if(this.isBacon(temp)) return true;
        return this.search(temp);
    },

    //Links targetWord to keyWord
    //Traverse through linked words,
    //return true if path from targetWord to keyWord exists
    isBacon: function(list){
        for(var i = 0; i < list.length; i++){
            if(list[i].word == this.targetWord.word) {
                //if targetWord is in list, set targetWord.next reference
                this.targetWord.next = list[i].next;
            }
        }
        var temp = this.targetWord;
        while(temp != null){
            if(temp.word == this.container[0][0].word){
                //Traverse linked wordNodes  until keyWord is found
                return true;
            }
            temp = temp.next;
        }
        return false;
    },

    //Set path from targetWord to keyWord
    //or set path of most elements form targetWord to keyWord
    setPath: function(){
        var temp = null; //targetWord reference
        if(this.searchStatus){
            temp = this.targetWord;
        } else {
            //last list in container
            var list = this.container[this.container.length - 1];
            var min = 130; //min distance between targetWord and list words
            var minIndex = -1; //index of wordNode with min distance from the targetWord
            var n = 0; //place holder for min value
            for(var i = 0; i < list.length; i++){
                n = 0;
                for(var j = 0; j < list[i].length; j++){
                    n += Math.abs((this.targetWord.word.charCodeAt(j) - 96) - (list[i].word.charCodeAt(j) - 96));
                }
                if(n < min){
                    min = n;
                    minIndex = i;
                }
            }
            temp = list[minIndex];
        }
        while(temp != null){
            this.path.push(temp);
            temp = temp.next;
        }
    },

    //Print path from targetWord to keyWord
    print: function(){
        $results = $("#results");
        $message = $('#message');
        $results.html("");

        var baconHappy = true;
        var textNode = $(document.createElement('p'));
        var list;
        var text = '';
        var txt = '';
        var t;
        var wordScoreEl;
        var score = 0;
        var wordScore = 0;
        var scoreInd;

        textNode.addClass("message");
        if(this.searchStatus) {

            text = 'A path from ' + this.keyWord + ' to ' + this.targetWord.word;
            textNode.append(text);
            $message.append(textNode);

            list = $(document.createElement('ul'));
            $results.append(list);

            for (var i = this.path.length - 1; i >= 0; i--) {
                txt = this.path[i].word.toLowerCase();
                wordScore = 0;
                for(var j = 0; j < txt.length; j++) {
                    scoreInd = this.alphabet.indexOf(txt[j].toUpperCase());
                    score += this.alphabetScore[scoreInd];
                    wordScore += this.alphabetScore[scoreInd];

                }
                (function(i,text,wordSco){
                    setTimeout(function(){
                        listEl = $(document.createElement('li'));
                        listEl.addClass("result-item list-group-item list-group-item-info").addClass("bounceIn animated");
                        t = document.createTextNode(text);
                        wordScoreEl = $(document.createElement('span'));
                        wordScoreEl.addClass('wordScore animated fadeOutUp');
                        wordScoreEl.append("+"+wordSco);
                        listEl.append(t);
                        listEl.append(wordScoreEl);
                        list.append(listEl);
                     },400*i);
                })(i,txt, wordScore);
            }
            score = score*5;
        }else{
            baconHappy = false;
            text += 'Sorry! No path from ' + this.keyWord + ' to ' + this.targetWord.word + '<br >\n';
            text += 'Closest Path:\n';
            textNode.append(text);
            $message.append(textNode);

            list = $(document.createElement('ul'));
            list.addClass('result-list list-group');
            $results.append(list);

            for(var i = this.path.length - 1; i >= 0; i--){
                txt = this.path[i].word.toLowerCase();
                wordScore = 0;
                for(var j = 0; j < txt.length; j++) {
                    scoreInd = this.alphabet.indexOf(txt[j].toUpperCase());
                    score += this.alphabetScore[scoreInd];
                    wordScore += this.alphabetScore[scoreInd];
                }
                (function(i,text,wordSco){
                    setTimeout(function(){
                        listEl = $(document.createElement('li'));
                        listEl.addClass("result-item list-group-item list-group-item-info").addClass("bounceIn animated");
                        t = document.createTextNode(text);
                        wordScoreEl = $(document.createElement('span'));
                        wordScoreEl.addClass('wordScore animated fadeOutUp');
                        wordScoreEl.append("+"+wordSco);
                        listEl.append(t);
                        listEl.append(wordScoreEl);
                        list.append(listEl);
                     },400*i);
                })(i,txt, wordScore);
            }
        }
        var rand = Math.floor(Math.random()*3)+1;
        if(baconHappy)
            $(".bacometer").attr('src',"../../static/images/kbhappy"+rand+".jpg");
        else
            $(".bacometer").attr('src',"../../static/images/kbsad"+rand+".jpg");
        $(".bacometer").fadeIn();
        $('#score').text("Score: "+score);

        $.ajax("../send_score", {
                method: 'POST',
                data: {
                    score: score,
                    target:self.targetWord.word
                },
                success:function(data){

                },
                error:function(e){

                }

            }
        );
    }
}
