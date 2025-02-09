function formatCommentsForPostman(comments) {
    if (!Array.isArray(comments)) {
        console.error("Input should be an array of comments.");
        return;
    }

    const formattedJSON = {
        comments: comments.map(comment => comment.trim()) // Trim whitespace
    };

    // Convert to JSON string with double quotes
    const jsonString = JSON.stringify(formattedJSON, null, 4);

    console.log("Formatted JSON with double quotes:");
    console.log(jsonString); // Pretty-print JSON for verification

    return jsonString; // Return JSON string for sending to APIs
}

// Example usage with your comments
const comments = ['You can do it! Darr lagna galat baat nahi, darr ke bhagna galat baat hai', '4:58 "Do or die "- ab isko litterally mat lena', "guys please don't skip january attempt , i also th…as you will have someone to talk and share things", '4:58 Sir: Do or die \nKota students: Aight I’ma head out', 'Somewhere needed this video. Thank u sir.', 'Anup sir please daily ya to 20-30 mins ke liye gui…yuki akelapan aur anxiety peak par hai please sir', 'mere dimag ye hai ki jan attempt mein hai:\nagar>97…<95%ile then complete focus on boards to get 95+%', 'God has plan for everyone \n                   ~~virat kohli', 'sir ek session aap ya kunal sir lelejiye jisme liv…s saal 60+ ke liye ek video pls\neveryone pls vote', 'Thnkk yu sir much needed this time', 'Sir can I crack jee mains if I start preparing from now??', 'sir aaj 49 (18)aaya kuch samajh nhi aa rha mere fr…hle 83,53,80 tha pr math me20 se 25 lgbhag bn rha', 'Jis jiske L lag gye hain mocks me like', 'karna hai toh karna hai, kyuki hame kya karna hai\nPaper phodhna hai', 'Sir preparation kam hone ki wajah se bahut time se… attempt bhi utna hi imp hai jitna April attempt.', 'Sir bseb se hu 1 Feb se exam h but jee v h ..   je…practice nhi h , really frustrated hu sir kya kru', 'Sir marks app se bhi marks nhi aa rhe ab to', 'Sir 12th Feb ko board exam he kya karu', "95 percentile must in jan \nDon't target april", 'Sir 21 tk toh pre board h aur side s bio h 25 ko a…e baad 3 practical h aur phir pre board 2 Feb 1 s', 'Good evening Sir. I have given my best throughout … now. Just Mock test score improvement is needed.', '0:57 5% toh aya tha sir', 'Sir plss me zero pr hu aur mujhe April wala dena hai strategy bta do sir plss plsss', 'January is my final chance baki dekhi jayegi !!!', 'Revision toh pura ni hua priority d wale chap skip… ni aya jan me 99%ile laake adv pe focus krna hai', 'Sir mera 4 feb se bord exam hai lakin 1 % bhi dar nahi hai bord se', 'Paper phodna hai ..', 'paper phodna hai!!', 'Sir aapne jo important topic list di hai usme se j…t me jaunga to 95+ percentile aa sakti hai kya???', 'Thank you sir', 'Paper phodna hai!!', 'Yes sir paper phodna hai', 'Thank you so much sir', 'Sir ab sch mein nhi ho pa rha school vale practica…o jata hai jisse demotivate ho rhi hun mein bohot', 'I will sirr!! \n#comebackthistime #doordie #PAPERPHODNAHAI', 'If as a dropper you are scoring below 100 it means you have wasted whole year', 'Aaj ye log Jan attempt skip krre.. kal yehi log Ap…he nhi thi toh JEE/NEET wala rasta he kyu chuna??', 'padlo bhai 14 din hai 100 se 120 aajayenge agar abhi bhi sahi se padhlo toh', 'Vote for conic in oneshot', 'Sir im stuck at 150 in quizzr mocks', "Sir but I am thinking that ki agar mai apna left o…hi khraab ho skta hai..\nWhat's ur advice on this?", 'PAPER PHODNA HAI', 'Jan attempt is the last attempt', 'Paper phodunga.', 'Thank u very much sir needed this tooo much', 'Inorganic Chemistry ke revision session karwa dijiye sir please', 'Bhai main abhi start kr rha hu jan skip april me 98 percentile aa sakta h', 'paper phodke rhunga...', 'Todays qft', 'Prince sir pyqs video plss', 'rassi kharidne ka mn kr rha h sir bhut...', 'paper phodna hai!', 'Paper phodna hai!', 'Kis kiske mock test number below 100 marks', 'Sir cbse practicals but ill try my best', 'Sir i was feeling the same:)', 'Paper phodna h', 'Paper phodna hai', '#paperphodnahai', '#paperphodnahai', 'Paparpodhnahai', '#PaperPhodnaHai', '#PaperPhodhnaHai', 'NOT 0.0001% CHANCE THAT THIS THOUGHT WAS IN MY MIND', '3rd', "Mai v jan me nahi kar paunga,sorry sir but it's a reality"];

const formatted = formatCommentsForPostman(comments);