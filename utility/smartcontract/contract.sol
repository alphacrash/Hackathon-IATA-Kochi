pragma solidity ^0.4.0;
contract Contract {

    struct Agreement {
        string donator;
        string receiver;
    }

    Agreement[] private agreements;

    function addAgreement(string donator, string receiver) public {
        agreements.push(Agreement({
            donator: donator,
            receiver: receiver
        }));
    }

    function checkAgreements(string donator, string receiver) public constant returns (bool) {
        for (uint i = 0; i < agreements.length; i++) {
            if (compareStrings(agreements[i].donator, donator) && compareStrings(agreements[i].receiver, receiver)) {
                return true;
            }
        }

        return false;
    }

    function compareStrings (string a, string b) view returns (bool){
       return keccak256(a) == keccak256(b);
   }
}
