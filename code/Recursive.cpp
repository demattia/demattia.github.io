#include <iostream>
#include <vector>
#include <TLorentzVector.h>

/**
 * Recursive class to compute all possible unordered combinations of k elements out of N
 */

class Recursive
{
 public:

  Recursive(const std::vector<TLorentzVector> * inputJets) :
  jets(inputJets), k(1), DHT(0.)
  {
    N = jets->size();
    indeces = new unsigned int[N];
    for( unsigned int i=0; i<N; ++i ) {
      indeces[i] = i;
    }
  }
  ~Recursive()
  {
    delete indeces;
  }

  void getIndexArray()
  {
    for( k=1; k<N; ++k ) {
      unsigned int * indexArray = new unsigned int[k];
      getIndex(indexArray, 0, 0);
    }
  }

 protected:

  void getIndex(unsigned int * indexArray, const unsigned int id, const unsigned int recursiveIndex)
  {
    for( unsigned int i=id; i<N; ++i ) {
      std::cout << "i = " << i << std::endl;
      indexArray[recursiveIndex] = i;
      if(recursiveIndex < k-1) {
	getIndex(indexArray, i+1, recursiveIndex+1);
      }
      else {
	// The combination is available here
	for( unsigned int i=0; i<k; ++i ) {
	  std::cout << "indexArray["<<i<<"] = " << indexArray[i] << std::endl;
	}
	// Now loop on the vector and compute the DeltaHT variable
	std::vector<TLorentzVector> pseudoJetVector1;
	std::vector<TLorentzVector> pseudoJetVector2;
	std::vector<TLorentzVector>::const_iterator it = jets->begin();
	unsigned int indexId = 0;
	unsigned int jetId = 0;
	for( ; it != jets->end(); ++it, ++jetId ) {
	  if( (indexId < k) && (indexArray[indexId] == jetId) ) {
	    pseudoJetVector1.push_back(*it);
	    ++indexId;
	  }
	  else {
	    pseudoJetVector2.push_back(*it);
	  }
	}
	it = pseudoJetVector1.begin();
	TLorentzVector pseudoJet1(*it);
	++it;
	for( ; it != pseudoJetVector1.end(); ++it ) {
	  pseudoJet1 += *it;
	}
	it = pseudoJetVector2.begin();
	TLorentzVector pseudoJet2(*it);
	++it;
	for( ; it != pseudoJetVector2.end(); ++it ) {
	  pseudoJet2 += *it;
	}
	double DeltaHT = pseudoJet1.Pt() - pseudoJet2.Pt();
	std::cout << "DeltaHT = " << DeltaHT << std::endl;
	if( DeltaHT < DHT ) DHT = DeltaHT;
      }
    }  
  }

  const std::vector<TLorentzVector> * jets;
  unsigned int k;
  double DHT;
  unsigned int N;
  unsigned int * indeces;
};

int test()
{
  std::vector<TLorentzVector> jets;
  jets.push_back(TLorentzVector(1., 0., 0., 2.));
  jets.push_back(TLorentzVector(-0.5, 0., 0., 2.));
/*  jets.push_back(TLorentzVector(0., 0., 0., 0.));
  jets.push_back(TLorentzVector(0., 0., 0., 0.));
  jets.push_back(TLorentzVector(0., 0., 0., 0.));*/
  Recursive rec(&jets);
  rec.getIndexArray();
  return 0;
}